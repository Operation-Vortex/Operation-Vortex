import 'package:clean_architecure_demo/domain/entities/barber.dart';

abstract class BarberRepository {
  Future<List<Barber>> getBarbers();
  Future<Barber> getBarberById(String id);
}
