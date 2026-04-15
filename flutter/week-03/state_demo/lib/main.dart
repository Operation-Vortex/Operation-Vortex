import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:state_demo/providers.dart';

void main() => runApp(const ProviderScope(child: MyApp()));

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: CurrentBarberScreen(),
    );
  }
}

class CurrentBarberScreen extends ConsumerWidget {
  const CurrentBarberScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final appointmentsAsync = ref.watch(currentBarberAppointmentsProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('My Appointments')),
      body: Column(
        children: [
          ElevatedButton(
            onPressed: () => ref.read(currentUserProvider.notifier).login('B001'),
            child: const Text('Login as B001'),
          ),
          ElevatedButton(
            onPressed: () => ref.read(currentUserProvider.notifier).login('B002'),
            child: const Text('Login as B002'),
          ),
          ElevatedButton(
            onPressed: () => ref.read(currentUserProvider.notifier).logout(),
            child: const Text('Logout'),
          ),
          Expanded(
            child: appointmentsAsync.when(
              loading: () => const Center(child: CircularProgressIndicator()),
              error: (error, stack) => Center(child: Text('Error: $error')),
              data: (appointments) => appointments.isEmpty
                  ? const Center(child: Text('No user logged in'))
                  : ListView.builder(
                      itemCount: appointments.length,
                      itemBuilder: (context, index) => ListTile(
                        title: Text(appointments[index]),
                      ),
                    ),
            ),
          ),
        ],
      ),
    );
  }
}