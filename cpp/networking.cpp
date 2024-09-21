#include "networking.h"
#include <LoRaLib.h>
#include <painlessMesh.h>

// LoRa object and Mesh Network object
LoRaClass LoRa;
painlessMesh mesh;

// Function to set up LoRa communication
void setupLoRa() {
    // Begin LoRa at the specified frequency
    if (!LoRa.begin(LORA_BAND)) {
        Serial.println("LoRa init failed!");
        while (1);
    }
    Serial.println("LoRa initialized successfully.");
}

// Function to send messages via LoRa
void sendLoRaMessage(const String& message) {
    LoRa.beginPacket();
    LoRa.print(message);
    LoRa.endPacket();
    Serial.printf("Sent message: %s\n", message.c_str());
}

// Function to set up Mesh Network
void setupMeshNetwork() {
    // Set up the mesh network
    mesh.setDebugMsgTypes(ERROR | STARTUP);  // Set mesh debugging level
    mesh.init("MyMesh", "password123", 5555); // Mesh network with SSID and port
    mesh.onReceive(&onMessageReceived); // Handle message reception
    Serial.println("Mesh network initialized successfully.");
}

// Callback for when a message is received
void onMessageReceived(uint32_t from, String& msg) {
    Serial.printf("Received message: %s from %u\n", msg.c_str(), from);
    // Optionally, handle the message (e.g., store it, process it, etc.)
}

// Function to send location data over LoRa
void sendLocationData(float latitude, float longitude) {
    String locationMessage = "Location: " + String(latitude) + "," + String(longitude);
    sendLoRaMessage(locationMessage);
}

// Function to periodically resend unsent messages
void resendUnsentMessages() {
    // Implement your logic to retrieve and resend unsent messages
    // For example, if you have a list of unsent messages stored in a variable
    // Iterate through them and send them using sendLoRaMessage(message)
}
