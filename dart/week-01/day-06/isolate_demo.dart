import 'dart:isolate';

// Heavy computation
int heavyComputation(int n) {
  int result = 0;
  for (int i = 0; i < n; i++) {
    result += i;
  }
  return result;
}

// This function runs in a separate isolate
void isolateFunction(SendPort sendPort) {
  int result = heavyComputation(100000000);
  sendPort.send(result);
}

void main() async {
  print("Main isolate: starting");
  print("Main isolate: UI would be rendering here");

  // Create a ReceivePort to get results back
  ReceivePort receivePort = ReceivePort();

  // Spawn a new isolate
  await Isolate.spawn(isolateFunction, receivePort.sendPort);

  // Wait for result without blocking UI
  int result = await receivePort.first;

  print("Main isolate: got result: $result");
  print("Main isolate: UI stayed responsive the whole time");

  receivePort.close();
}
