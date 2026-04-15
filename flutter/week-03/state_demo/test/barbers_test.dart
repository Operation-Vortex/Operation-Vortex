import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:state_demo/providers.dart';

void main() {
  test('barbers list loads with fake data', () async {
    final container = ProviderContainer(
      overrides: [
        barbersProvider.overrideWith((ref) async {
          return ['Fake Barber 1', 'Fake Barber 2', 'Fake Barber 3'];
        }),
      ],
    );

    final barbers = await container.read(barbersProvider.future);

    expect(barbers.length, equals(3));
    expect(barbers.first, equals('Fake Barber 1'));

    container.dispose();
  });
}