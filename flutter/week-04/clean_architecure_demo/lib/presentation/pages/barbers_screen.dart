import 'package:clean_architecure_demo/presentation/providers/barber_provider.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class BarbersScreen extends ConsumerWidget {
  const BarbersScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final barbersAsync = ref.watch(barbersProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('CutAbove Barbers')),
      body: barbersAsync.when(
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (error, stack) => Center(child: Text('Error: $error')),
        data: (barbers) => ListView.builder(
          itemCount: barbers.length,
          itemBuilder: (context, index) {
            final barber = barbers[index];
            return ListTile(
              title: Text(barber.name),
              subtitle: Text(barber.phone),
              trailing: Text(
                'GHS ${(barber.earnings / 100).toStringAsFixed(2)}',
                style: TextStyle(
                  color: barber.isActive ? Colors.green : Colors.grey,
                ),
              ),
              leading: CircleAvatar(
                backgroundColor: barber.isActive ? Colors.green : Colors.grey,
                child: Text(barber.name[0]),
              ),
            );
          },
        ),
      ),
    );
  }
}
