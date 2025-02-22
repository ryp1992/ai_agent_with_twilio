import asyncio
import websockets
import json
import base64
import os


async def send_audio(uri, audio_file_path):
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected to WebSocket at {uri}")

            # Simulate the initial 'start' message (important!)
            start_message = {
                "event": "start",
                "streamSid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Dummy stream SID
            }
            await websocket.send(json.dumps(start_message))

            with open(audio_file_path, "rb") as f:
                while True:
                    chunk = f.read(1024)  # Adjust chunk size as needed
                    if not chunk:
                        break

                    # Base64 encode the audio chunk
                    audio_base64 = base64.b64encode(chunk).decode('utf-8')

                    media_message = {
                        "event": "media",
                        "streamSid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Must match the 'start' message
                        "media": {"payload": audio_base64, "timestamp": 0}  # Add a timestamp
                    }
                    await websocket.send(json.dumps(media_message))

                    await asyncio.sleep(0.02)  # Simulate real-time audio (adjust as needed)

            print("Audio file sent completely")

            # Simulate the 'stop' message (important!)
            stop_message = {
                "event": "stop",
                "streamSid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Must match the 'start' message
            }
            await websocket.send(json.dumps(stop_message))

    except Exception as e:
        print(f"Error: {e}")


async def main():
    uri = "ws://localhost:5050/media-stream"
    audio_file_path = "/Users/rahulparikh/projects/twilloAI/recorded_audio.wav"  # Your local audio file
    await send_audio(uri, audio_file_path)


if __name__ == "__main__":
    asyncio.run(main())
