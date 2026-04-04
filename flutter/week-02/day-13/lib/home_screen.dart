import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home - Feature Version')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () => context.push('/login'),
              child: const Text('Go to Login'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () => context.push('/profile/42'),
              child: const Text('Go to Profile 42'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () => context.push('/settings'),
              child: const Text('Go to Settings'),
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () => context.push('/nonexistent'),
              child: const Text('Go to nowhere'),
            ),
            ElevatedButton(
              onPressed: () => context.push('/about'),
              child: const Text('Go to About'),
            )
          ],
        ),
      ),
    );
  }
}
