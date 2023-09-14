import cv2

captura = cv2.VideoCapture(0)
vid_counter = 0
vid=0

while True:
  if vid==0:
   codecs = cv2.VideoWriter_fourcc(*'MP4V')
   salida = cv2.VideoWriter('video_{}.mp4'.format(vid_counter),codecs,20.0,(640,480))
   vid_counter+=1
   vid=1
g)

  if ret == True:
    cv2.imshow('video', imagen) 
  
    if cv2.waitKey(1) & 0xFF == ord('a'):
      cv2.destroyAllWindows()
      vid=0
      while True:
         ret, imagen = captura.read()
         cv2.imshow('video', imagen) 
         salida.write(imagen)
         if cv2.waitKey(1) & 0xFF == ord('q'):
              break

captura.release()
salida.release()
cv2.destroyAllWindows()
