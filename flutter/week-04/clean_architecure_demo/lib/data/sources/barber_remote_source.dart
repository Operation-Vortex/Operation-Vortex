import '../models/barber_model.dart';

class BarberRemoteSource {
  // In real CutAbove — this would use Dio to call Newman's API
  // For now — fake data simulating an API response

  Future<List<BarberModel>> getBarbers() async {
    await Future.delayed(Duration(seconds: 1)); // simulate network delay

    final fakeResponse = [
      {
        'id': '1',
        'name': 'Kwame',
        'phone': '0241234567',
        'is_active': true,
        'earnings': 45000,
      },
      {
        'id': '2',
        'name': 'Kofi',
        'phone': '0559876543',
        'is_active': true,
        'earnings': 38000,
      },
      {
        'id': '3',
        'name': 'Ama',
        'phone': '0201234567',
        'is_active': false,
        'earnings': 52000,
      },
    ];

    return fakeResponse.map((json) => BarberModel.fromJson(json)).toList();
  }

  Future<BarberModel> getBarberById(String id) async {
    await Future.delayed(Duration(milliseconds: 500));

    final barbers = await getBarbers();
    return barbers.firstWhere((b) => b.id == id);
  }
}
