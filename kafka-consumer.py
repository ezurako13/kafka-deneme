from kafka import KafkaConsumer
import json

# Initialize the consumer
consumer = KafkaConsumer(
    'user_events',  # Topic to subscribe to
    bootstrap_servers='kafka:9092',  # Kafka broker
    auto_offset_reset='earliest',  # Start reading from the beginning if no offset is present
    enable_auto_commit=True,  # Automatically commit message offsets
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserialize JSON messages
)

# Continuously listen for new messages
for message in consumer:
    print(f"Received message: {message.value}")

# docker exec -it docker-kafka-1 /usr/bin/kafka-console-consumer --topic test-topic --from-beginning --bootstrap-server kafka:9092
# docker exec -it docker-zookeeper-1 /usr/bin/kafka-console-producer --topic test-topic --bootstrap-server kafka:9092


# 01.10.2024 Sali:
#     - Bursiyerligim basladi.
#     - Gerekli hesaplarim acildi.

# 04.10.2024 Cuma:
#     - SNS servisimizde calisabilmek adina servisin, temeli olan massage broker'lar hakkinda arastima yaptim.
#     - Ozellikle bizim de SNS servisimizin icerisinde kullandigimiz Kafka'yi ogrenmeye calistim.

# 08.10.2024 Sali:
#     - SNS servisimize eklemek istedigimiz Nats massege broker'ini arastirdim.
#     - Ogrendiklerimi kalici hale getirmek icin kenime bir test kurulumu yapmaya calistim.
#     - Test ortamim icin cihazima local bir docker kurulumu yaptim.

# 11.10.2024 Cuma:
#     - Message broker'larin temel userlari olan producer ve consumer'i temsil etmesi icin 
# iki adet container olusturup iclerine kafka ve zookeeper kullanarak birer script hazirladim.
#     //- Farkli kullanim alanlari icin de uygun senaryolar olusturup test kodlarini gozlemloyorum.
#     //- Buradan sonra Nats kurulumunu, yine kendi bilgisayarima, yapmaya calisacagim.