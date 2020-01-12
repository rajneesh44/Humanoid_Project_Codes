import pyaudio
p = pyaudio.PyAudio()
for li in range(p.get_device_count()):
    print(p.get_device_info_by_index(li).get('name'),li)