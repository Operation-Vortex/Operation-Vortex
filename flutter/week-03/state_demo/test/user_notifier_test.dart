import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:state_demo/providers.dart';

void main() {
  test('user is null when app starts', () {
    final container = ProviderContainer();
    
    final user = container.read(currentUserProvider);
    
    expect(user, isNull);
    
    container.dispose();
  });

  test('user is set after login', () {
    final container = ProviderContainer();
    
    container.read(currentUserProvider.notifier).login('B001');
    
    final user = container.read(currentUserProvider);
    
    expect(user, equals('B001'));
    
    container.dispose();
  });

  test('user is null after logout', () {
    final container = ProviderContainer();
    
    container.read(currentUserProvider.notifier).login('B001');
    container.read(currentUserProvider.notifier).logout();
    
    final user = container.read(currentUserProvider);
    
    expect(user, isNull);
    
    container.dispose();
  });
}