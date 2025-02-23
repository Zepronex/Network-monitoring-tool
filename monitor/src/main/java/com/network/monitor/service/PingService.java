package com.network.monitor.service;

import org.springframework.stereotype.Service;

@Service
public class PingService {
    public PingResult pingWithLatency(String ipAddress) { ... }
}
