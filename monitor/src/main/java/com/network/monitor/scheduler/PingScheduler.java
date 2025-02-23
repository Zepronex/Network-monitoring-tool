package com.network.monitor.scheduler;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class PingScheduler {
    @Scheduled(fixedRate = 30000)
    public void checkAllDevices() { ... }
}
