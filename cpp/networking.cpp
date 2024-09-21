#include "networking.h"
#include <LoRaLib.h>
#include <painlessMesh.h>

// LoRa object and Mesh Network object
LoRaClass LoRa;
painlessMesh mesh;

// Function to set up LoRa communication
void setupLoRa() {
    // Begin LoRa at the specified frequency
    LoRa.begin(LORA_BAND);
}

// Function to send messages via LoRa
void sendLoRaMessage(const String& message) {
    LoRa.beginPacket();
    LoRa.print(message);
    LoRa.endPacket();
}

// Function to set up Mesh Network
void setupMeshNetwork() {
    // Set up the mesh network
    mesh.setDebugMsgTypes(ERROR | STARTUP);  // Set mesh debugging level
    mesh.init("MyMesh", "password123", 5555); // Mesh network with SSID and port
    mesh.onReceive(&onMessageReceived); // Handle message reception
}

// Callback for when a message is received
void onMessageReceived(uint32_t from, String &msg) {
    Serial.printf("Received message: %s from %u\n", msg.c_str(), from);
}

