import 'dart:io';

class DirectoryAnalysisResult {
  int totalFiles;
  int totalSize;
  File? largestFile;
  int largestFileSize;
  Map<String, int> extensionTypeMap;

  DirectoryAnalysisResult(
    this.totalFiles,
    this.totalSize,
    this.largestFile,
    this.largestFileSize,
    this.extensionTypeMap,
  );
}

bool validateDirectory(Directory directoryPath) {
  if (!directoryPath.existsSync()) {
    print('Error: Directory does not exist.');
    return false;
  }

  return true;
}

DirectoryAnalysisResult analyzeDirectory(Directory directoryPath) {
  List<FileSystemEntity> itemsInDirectory = directoryPath.listSync();

  int totalFiles = 0;
  int totalSize = 0;
  File? largestFile;
  int largestFileSize = 0;
  Map<String, int> extensionTypeMap = {};

  for (FileSystemEntity currentItemUnderIteration in itemsInDirectory) {
    if (currentItemUnderIteration is File) {
      totalFiles = totalFiles + 1;

      int currentItemSize = currentItemUnderIteration.lengthSync();
      totalSize = totalSize + currentItemSize;

      if (currentItemSize > largestFileSize) {
        largestFileSize = currentItemSize;
        largestFile = currentItemUnderIteration;
      }

      String filePath = currentItemUnderIteration.path;
      String fileName = filePath.split('/').last;

      String fileExtension;

      if (fileName.contains('.')) {
        fileExtension = '.' + fileName.split('.').last;
      } else {
        fileExtension = '[no extension]';
      }

      if (extensionTypeMap.containsKey(fileExtension)) {
        extensionTypeMap[fileExtension] =
            extensionTypeMap[fileExtension]! + 1;
      } else {
        extensionTypeMap[fileExtension] = 1;
      }
    }
  }

  return DirectoryAnalysisResult(
    totalFiles,
    totalSize,
    largestFile,
    largestFileSize,
    extensionTypeMap,
  );
}

void printReport(
  Directory directoryPath,
  DirectoryAnalysisResult analysisResult,
) {
  print('FILE SYSTEM ANALYSIS');
  print('--------------------');
  print('Directory: ${directoryPath.path}');
  print('Total files: ${analysisResult.totalFiles}');
  print('Total size: ${analysisResult.totalSize} bytes');

  if (analysisResult.largestFile != null) {
    print('Largest file: ${analysisResult.largestFile!.path}');
    print('Largest file size: ${analysisResult.largestFileSize} bytes');
  } else {
    print('Largest file: None');
    print('Largest file size: 0 bytes');
  }

  print('File type breakdown:');
  analysisResult.extensionTypeMap.forEach((fileExtension, count) {
    print('$fileExtension: $count');
  });
}

void runAnalyzer(String userInputPath) {
  Directory directoryPath = Directory(userInputPath);

  bool isValidDirectory = validateDirectory(directoryPath);

  if (!isValidDirectory) {
    return;
  }

  DirectoryAnalysisResult analysisResult = analyzeDirectory(directoryPath);

  printReport(directoryPath, analysisResult);
}

void main(List<String> arguments) {
  if (arguments.isEmpty) {
    print('Usage: dart run analyzer.dart <directory_path>');
    return;
  }

  String userInputPath = arguments[0];

  runAnalyzer(userInputPath);
}