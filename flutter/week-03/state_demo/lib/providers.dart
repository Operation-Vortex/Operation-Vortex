import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_riverpod/legacy.dart';

Future<List<String>> fetchBarbers() async {
  await Future.delayed(Duration(seconds: 2));
  return ['Barber A', 'Barber B', 'Barber C'];
}

final barbersProvider = FutureProvider<List<String>>((ref) async {
  return fetchBarbers();
});

final clockProvider = StreamProvider<String>((ref) async* {
  while (true) {
    await Future.delayed(Duration(seconds: 1));
    final now = DateTime.now();
    yield '${now.hour}:${now.minute}:${now.second}';
  }
});

final barberAppointmentsProvider = FutureProvider.autoDispose.family<List<String>, String>((
  ref,
  barberId,
) async {
  await Future.delayed(Duration(seconds: 1));
  return [
    "Appointment 1 for $barberId",
    "Appointment 2 for $barberId",
    "Appointment 3 for $barberId",
  ];
});

class CurrentUserNotifier extends StateNotifier<String?> {
  CurrentUserNotifier() : super(null);

  void login(String userId) {
    state = userId;
  }

  void logout() {
    state = null;
  }
}

final currentUserProvider = StateNotifierProvider<CurrentUserNotifier, String?>((ref) {
  return CurrentUserNotifier();
});

final currentBarberAppointmentsProvider = FutureProvider.autoDispose<List<String>>((ref) async {
  final userId = ref.watch(currentUserProvider);

  if (userId == null) {
    return [];
  }

  final appointments = await ref.watch(barberAppointmentsProvider(userId).future);
  return appointments;
});

class User {
  final String id;
  final String name;
  User({required this.id, required this.name});
}


