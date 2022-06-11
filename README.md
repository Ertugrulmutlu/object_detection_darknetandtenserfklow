# object_detection_darknetandtenserfklow
# TÜRKÇE :
  Darknet ve TenserFlow'u birleştirerek daha hızlı ve verimli bir obje detektörü,
  Web kamerası ile çalışarak gerçek zamanlı, obje algılar,
  
  Yapmanız gerekenler:
  
    1- Dosyaları bir klasöre atınız,
    2- Cmd ile .py ile başlayan dosyanızı başlatın (Örneğin: python object_detection.py --config=yolo.cfg --weights=yolo.weight),
    3- Program çalışırken kamera izni isteyecek eğer istemezse çalışacak.
    
  Kendi modelinizi kullanmak için:
  
    1- ".cfg" dosyanız ile indirilen ".cfg" dosyanızı değiştirin,
    2- ".weights" dosyanız ile indirilen ".weights" dosyanızı değiştirin,
    3- "coco.names" adlı dosyayı silin veya klasör'den çıkarın,
    4- Kendi oluşturduğunuz "coco.names" dosyanızın adı farklı ile "coco.names" yapıp klasöre atın, Eğer adı "coco.names" ise sadece klasöre atın,
    5- Programı başlatın.
    
# ENGLISH :
  Fast and efficient object detection program combining Darknet and TensorFlow,
  Real time object detection by working with webcam
  
  How to works:
  
    1- Extract the files in folder
    2- With cmd, start .py file (Example:python object_detection.py --config=yolo.cfg --weights=yolo.weight )
    3- When the program is running, it will ask for camera permission, if it doesn't, it will work. 
    
 How to use program with own model:
 
    1- Replace the ".cfg" file with its own ".cfg" file,
    2- Replace the ".weights" file with its own ".weights" file,
    3- Delete the file named "coco.names" or remove it from the folder,
    4- If own made "coco.names" file named diferrent, change name to "coco.names" and put in folder, if not just put it in folder,
    5- Run Program
