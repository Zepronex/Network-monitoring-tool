package com.network.monitor.repository;

import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import com.network.monitor.model.Device;

public interface DeviceRepository extends JpaRepository<Device, Long> {
    Optional<Device> findByIpAddress(String ipAddress);
}