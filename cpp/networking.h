#ifndef NETWORKING_H
#define NETWORKING_H

#include <LoRaLib.h> // LoRa communication
#include <painlessMesh.h> // Mesh network

// Define LoRa settings
#define LORA_BAND 915E6 // Set the frequency to 915 MHz

// Function prototypes
void setupLoRa();
void sendLoRaMessage(const String& message);
void setupMeshNetwork();
void onMessageReceived(uint32_t from, String &msg);

#endif

