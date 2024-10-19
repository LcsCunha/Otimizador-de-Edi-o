from moviepy.video.io.VideoFileClip import VideoFileClip

# Função para dividir o vídeo em intervalos de 'interval' minutos
def divide_video(input_path, output_dir, interval, count_start=1):
    # Abrir o vídeo
    video = VideoFileClip(input_path)
    total_duration = video.duration  # duração total em segundos
    interval_seconds = int(interval * 60)  # converter minutos para segundos

    # Contador para nomear os clipes
    clip_count = count_start

    # Loop através do vídeo e criar subclips
    for start_time in range(0, int(total_duration), interval_seconds):
        # Definir os tempos de início e fim

        print(f"************Criando subclipe {clip_count}************\n")
        
        end_time = start_time + interval_seconds

        if end_time > total_duration:
            end_time = total_duration

        subclip = video.subclip(start_time, end_time)
        
        # Exportar o subclip para o diretório de saída
        output_path = f"{output_dir}/subclip_{clip_count}.mp4"
        subclip.write_videofile(output_path, codec="libx264", 
                                audio_codec="aac", threads=8)
        clip_count += 1

    # Fechar o vídeo
    video.close()

# Exemplo de uso
input_video_path = "C:/Videos brutos/19-10-2024/19-10-Clipe-Source-3.mp4"
pasta_destino = "C:/Videos brutos/19-10-2024"
duracao_subclip = 3  # em minutos
count_start = 1

divide_video(input_video_path, pasta_destino, duracao_subclip, count_start)