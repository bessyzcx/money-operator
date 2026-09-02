import Foundation
import Vision
import AppKit

struct OCRLine: Codable {
    let text: String
    let confidence: Float
    let x: Double
    let y: Double
    let w: Double
    let h: Double
}

struct OCRFile: Codable {
    let path: String
    let lines: [OCRLine]
}

let args = Array(CommandLine.arguments.dropFirst())
if args.isEmpty {
    fputs("Usage: swift ocr_images.swift image...\n", stderr)
    exit(2)
}

var results: [OCRFile] = []

for path in args {
    let url = URL(fileURLWithPath: path)
    let filename = url.lastPathComponent
    guard let image = NSImage(contentsOf: url),
          let tiff = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: tiff),
          let cgImage = bitmap.cgImage else {
        results.append(OCRFile(path: filename, lines: []))
        continue
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["zh-Hans", "en-US"]

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    try handler.perform([request])

    let lines = (request.results ?? []).compactMap { observation -> OCRLine? in
        guard let candidate = observation.topCandidates(1).first else { return nil }
        let box = observation.boundingBox
        return OCRLine(
            text: candidate.string,
            confidence: candidate.confidence,
            x: box.origin.x,
            y: box.origin.y,
            w: box.width,
            h: box.height
        )
    }.sorted { left, right in
        if abs(left.y - right.y) > 0.01 { return left.y > right.y }
        return left.x < right.x
    }

    results.append(OCRFile(path: filename, lines: lines))
}

let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .withoutEscapingSlashes]
let data = try encoder.encode(results)
FileHandle.standardOutput.write(data)
