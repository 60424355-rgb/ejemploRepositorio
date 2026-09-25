import tkinter as tk
import numpy as np
import sounddevice as sd

# Configuración del audio
SAMPLE_RATE = 44100  # Frecuencia de muestreo (Hz)
CHUNK_SIZE = 1024    # Tamaño del bloque de audio
NUM_BARS = 32        # Cantidad de barras en el espectro

class EspectroAudio:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Espectro de Sonido")
        
        # Dimensiones de la ventana
        self.width = 600
        self.height = 300
        
        # Canvas de Tkinter
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # Creación inicial de las barras en el Canvas
        self.bar_width = self.width / NUM_BARS
        self.bars = []
        for i in range(NUM_BARS):
            x0 = i * self.bar_width
            x1 = x0 + self.bar_width - 2
            # Se crean rectángulos vacíos apoyados en el fondo (self.height)
            bar = self.canvas.create_rectangle(x0, self.height, x1, self.height, fill="#00FFCC", outline="")
            self.bars.append(bar)

        # Buffer para almacenar los datos del micrófono
        self.audio_data = np.zeros(CHUNK_SIZE)

        # Inicialización del flujo de micrófono en segundo plano
        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            blocksize=CHUNK_SIZE,
            callback=self.audio_callback
        )
        self.stream.start()

        # Iniciar ciclo de actualización del dibujo
        self.actualizar_espectro()

    def audio_callback(self, indata, frames, time, status):
        """Callback ejecutado por sounddevice cuando hay nuevos datos del micrófono."""
        self.audio_data = indata[:, 0]

    def actualizar_espectro(self):
        """Calcula la FFT de la señal y redimensiona las barras en el Canvas."""
        # 1. Transformada de Fourier para obtener amplitudes de frecuencia
        fft_data = np.abs(np.fft.rfft(self.audio_data))

        # 2. Dividir las frecuencias en subgrupos (tantos como barras)
        spectrum = np.array_split(fft_data[:CHUNK_SIZE // 2], NUM_BARS)
        
        # 3. Actualizar la altura de cada barra
        for i, chunk in enumerate(spectrum):
            # Promedio de la amplitud del bloque ajustado con un factor de ganancia
            magnitud = np.mean(chunk) * 15  
            
            # Limitar la altura al tamaño del Canvas
            altura_barra = min(magnitud * self.height, self.height)
            
            # Recalcular coordenadas del rectángulo (x0, y0, x1, y1)
            x0 = i * self.bar_width
            y0 = self.height - altura_barra
            x1 = x0 + self.bar_width - 2
            y1 = self.height
            
            self.canvas.coords(self.bars[i], x0, y0, x1, y1)

        # Volver a ejecutar esta función tras 30 ms (~30 FPS)
        self.root.after(30, self.actualizar_espectro)

    def cerrar(self):
        """Detiene el flujo de audio al cerrar la ventana."""
        self.stream.stop()
        self.stream.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EspectroAudio(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar)
    root.mainloop()