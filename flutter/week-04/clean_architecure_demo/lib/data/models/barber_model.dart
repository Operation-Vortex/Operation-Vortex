import '../../domain/entities/barber.dart';

class BarberModel extends Barber {
  const BarberModel({
    required super.id,
    required super.name,
    required super.phone,
    required super.isActive,
    required super.earnings,
  });

  factory BarberModel.fromJson(Map<String, dynamic> json) {
    return BarberModel(
      id: json['id'].toString(),
      name: json['name'] as String,
      phone: json['phone'] as String,
      isActive: json['is_active'] as bool,
      earnings: json['earnings'] as int,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'phone': phone,
      'is_active': isActive,
      'earnings': earnings,
    };
  }
}
