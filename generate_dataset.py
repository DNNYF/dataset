#!/usr/bin/env python3
"""
High-quality Dataset Generator for Indramayu Tourism
Generates conversational AI training data with detailed, rich content
"""

import json
import random
from typing import List, Dict, Tuple

class IndramayuDatasetGenerator:
    def __init__(self):
        self.topics = self.load_topics()
        self.question_templates = self.get_question_templates()
        self.location_data = self.get_location_data()
        
    def load_topics(self) -> List[str]:
        """Load topics from list-topik.txt"""
        topics = []
        try:
            with open('list-topik.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith(('Berikut', '.')):
                        if not line.isdigit():
                            topics.append(line)
        except FileNotFoundError:
            print("Error: list-topik.txt not found")
            return []
        return topics
    
    def get_question_templates(self) -> List[str]:
        """Get various question templates for generating diverse questions"""
        return [
            "Bisakah Anda menjelaskan tentang {topic}?",
            "Apa yang menarik dari {topic}?", 
            "Ceritakan tentang {topic}.",
            "Bagaimana sejarah {topic}?",
            "Apa saja aktivitas yang bisa dilakukan di {topic}?",
            "Di mana lokasi {topic}?",
            "Bagaimana cara menuju {topic}?",
            "Apa saja fasilitas di {topic}?",
            "Kapan waktu terbaik mengunjungi {topic}?",
            "Apakah {topic} cocok untuk wisata keluarga?",
            "Apa yang unik dari {topic}?",
            "Makanan khas apa yang ada di {topic}?",
            "Berapa biaya masuk ke {topic}?",
            "Apa tips berkunjung ke {topic}?",
            "Bagaimana kondisi {topic} saat ini?",
            "Apa saja yang ada di {topic}?",
            "Apakah ada festival atau acara khusus di {topic}?",
            "Apakah ada acara khusus di {topic}?"
        ]
    
    def get_location_data(self) -> Dict[str, Dict]:
        """Detailed information about each location"""
        return {
            "Pulau Biawak": {
                "type": "pulau",
                "history": "Pulau Biawak merupakan pulau kecil yang terletak di utara Pantai Karangsong. Nama 'Biawak' berasal dari populasi biawak liar yang menghuni pulau ini secara alami sejak ratusan tahun lalu.",
                "location": "sekitar 40 km dari pusat kota Indramayu, dapat diakses melalui Pelabuhan Karangsong dengan perjalanan perahu selama 3-4 jam",
                "attractions": "pengamatan biawak di habitat asli, pantai berpasir putih dengan air laut jernih, snorkeling, diving, dan menikmati sunset yang menakjubkan",
                "culture": "tempat yang dianggap sakral oleh masyarakat setempat dan sering dijadikan lokasi ritual tradisional nelayan",
                "events": "festival konservasi biawak yang diadakan setiap tahun untuk edukasi pelestarian satwa"
            },
            "Pantai Karangsong": {
                "type": "pantai",
                "history": "Pantai Karangsong telah menjadi pelabuhan nelayan utama di Indramayu sejak era kolonial Belanda. Nama 'Karangsong' berasal dari kata 'karang' dan 'song' yang berarti batu karang yang menyerupai rumah tradisional.",
                "location": "terletak di Desa Karangsong, Kecamatan Indramayu, sekitar 35 km dari pusat kota Indramayu",
                "attractions": "pelabuhan perikanan tradisional, pasar ikan segar, wisata kuliner seafood, dan pemandangan sunset di dermaga nelayan",
                "culture": "pusat kehidupan nelayan tradisional dengan berbagai upacara adat laut seperti Nadran dan Sedekah Laut",
                "events": "upacara Nadran setiap bulan Suro, festival kuliner seafood, dan pasar ikan harian di pagi dan sore hari"
            },
            "Hutan Mangrove Karangsong": {
                "type": "hutan",
                "history": "Hutan Mangrove Karangsong merupakan kawasan konservasi yang dikembangkan sejak tahun 1990-an sebagai upaya pelestarian ekosistem pesisir dan pencegahan abrasi pantai.",
                "location": "berada di area pesisir Desa Karangsong, dapat diakses melalui jalan raya Indramayu-Cirebon kemudian menuju pantai",
                "attractions": "jembatan kayu sepanjang 500 meter, pengamatan burung langka, wisata edukasi ekosistem mangrove, dan spot fotografi alam",
                "culture": "dijadikan lokasi edukasi konservasi alam bagi masyarakat setempat dan sebagai penyangga kehidupan nelayan tradisional",
                "events": "program penanaman mangrove setiap bulan, tour edukasi konservasi, dan kegiatan birdwatching"
            },
            "Pantai Tirtamaya": {
                "type": "pantai",
                "history": "Pantai Tirtamaya mulai dikembangkan sebagai destinasi wisata pada tahun 2000-an. Nama 'Tirtamaya' berasal dari bahasa Sanskerta yang berarti 'air suci yang indah'.",
                "location": "terletak di Desa Tirtamaya, Kecamatan Indramayu, sekitar 25 km dari pusat kota dengan akses jalan yang mudah",
                "attractions": "pantai dengan ombak tenang cocok untuk berenang, area bermain anak, warung kuliner seafood, dan gazebo untuk bersantai",
                "culture": "menjadi tempat rekreasi favorit keluarga dan sering dijadikan lokasi acara syukuran masyarakat setempat",
                "events": "festival pantai bersih setiap bulan, kompetisi memancing, dan pertunjukan seni budaya lokal di akhir pekan"
            },
            "Masjid Agung Indramayu": {
                "type": "masjid",
                "history": "Masjid Agung Indramayu dibangun pada abad ke-15 oleh Sultan Wiralodra sebagai pusat kegiatan keagamaan Islam di wilayah Indramayu. Arsitekturnya memadukan gaya Jawa dan Arab.",
                "location": "berada di jantung kota Indramayu, Jalan Jenderal Sudirman, mudah diakses dengan berbagai transportasi umum",
                "attractions": "arsitektur klasik dengan ornamen ukiran kayu Jawa, mihrab berornamen kaligrafi Arab, dan halaman luas untuk kegiatan komunal",
                "culture": "pusat kegiatan keagamaan dan sosial masyarakat Indramayu, tempat pengajian akbar dan perayaan hari besar Islam",
                "events": "shalat Idul Fitri dan Idul Adha, pengajian akbar setiap Jumat, dan kajian rutin setiap malam"
            },
            "Makam Raden Arya Wiralodra": {
                "type": "makam",
                "history": "Makam Raden Arya Wiralodra adalah tempat peristirahatan terakhir pendiri Kabupaten Indramayu pada abad ke-15. Beliau adalah sosok yang sangat dihormati dan dianggap sebagai wali penyebar Islam di wilayah ini.",
                "location": "terletak di kompleks pemakaman Panjunan, Kelurahan Panjunan, Kecamatan Indramayu, dekat dengan pusat kota",
                "attractions": "makam berarsitektur Jawa kuno dengan cungkup kayu jati, halaman luas dengan pohon-pohon tua, dan museum mini sejarah Indramayu",
                "culture": "tempat ziarah dan spiritual yang sangat dihormati masyarakat Indramayu, sering dikunjungi untuk meminta berkah dan doa",
                "events": "haul Raden Arya Wiralodra setiap tahun, ziarah massal saat bulan Ramadan, dan upacara tradisional Jawa"
            },
            "Tugu Mangga": {
                "type": "tugu",
                "history": "Tugu Mangga dibangun sebagai simbol kebanggaan Indramayu yang terkenal dengan Mangga Gedong Gincu berkualitas premium. Tugu ini diresmikan pada tahun 2005 sebagai landmark kota.",
                "location": "terletak di pusat kota Indramayu, tepatnya di persimpangan jalan utama yang menghubungkan berbagai wilayah kabupaten",
                "attractions": "tugu setinggi 15 meter berbentuk mangga raksasa, taman kota dengan berbagai tanaman hias, dan area kuliner malam hari",
                "culture": "menjadi identitas kota Indramayu dan simbol kejayaan pertanian mangga yang telah mengharumkan nama daerah",
                "events": "Festival Mangga Gedong Gincu setiap bulan Juli-Agustus, pameran produk lokal, dan pertunjukan budaya"
            },
            "Festival Mangga Gedong Gincu (event tahunan)": {
                "type": "festival",
                "history": "Festival Mangga Gedong Gincu pertama kali diadakan pada tahun 2008 sebagai upaya promosi mangga unggulan Indramayu yang telah mendapat sertifikat internasional. Festival ini menjadi ajang bangga masyarakat petani mangga.",
                "location": "diselenggarakan di berbagai lokasi strategis di Indramayu, dengan pusat acara di Alun-alun Puspawangi dan Tugu Mangga",
                "attractions": "pameran mangga dari berbagai petani, lomba makan mangga, demo pengolahan produk mangga, dan bazaar kuliner khas Indramayu",
                "culture": "merayakan hasil panen mangga terbaik dan melestarikan tradisi pertanian yang sudah turun-temurun di masyarakat Indramayu",
                "events": "diadakan setiap bulan Juli-Agustus selama musim panen mangga, meliputi parade, kompetisi, dan pertunjukan seni budaya"
            },
            "Upacara Adat Nadran (event tahunan)": {
                "type": "upacara",
                "history": "Upacara Nadran adalah tradisi turun-temurun masyarakat nelayan Indramayu yang telah berlangsung selama ratusan tahun. Nadran berasal dari kata 'nadzar' yang berarti janji atau sumpah kepada Yang Maha Kuasa.",
                "location": "dilaksanakan di berbagai pantai di Indramayu, terutama Pantai Karangsong, dengan prosesi menuju laut lepas menggunakan perahu tradisional",
                "attractions": "prosesi larung sesaji ke laut, pertunjukan kesenian tradisional seperti tari topeng, wayang kulit, dan musik tradisional Tarling",
                "culture": "tradisi syukur nelayan atas hasil tangkapan ikan dan permohonan keselamatan dalam melaut, mencerminkan hubungan harmonis manusia dengan alam",
                "events": "diadakan setiap bulan Suro (Muharram) dalam penanggalan Jawa, meliputi berbagai ritual dan perayaan selama satu minggu penuh"
            }
        }
    
    def generate_question(self, topic: str) -> str:
        """Generate a natural question about the topic"""
        template = random.choice(self.question_templates)
        return template.format(topic=topic)
    
    def generate_detailed_answer_id(self, topic: str, question: str) -> str:
        """Generate detailed answer in Bahasa Indonesia"""
        data = self.location_data.get(topic, {})
        
        if not data:
            # Generic fallback for topics not in detailed data
            return self.generate_generic_answer_id(topic)
        
        # Build detailed 3-paragraph answer
        paragraphs = []
        
        # Paragraph 1: Introduction and History
        history = data.get('history', f"{topic} merupakan salah satu destinasi menarik di Indramayu yang memiliki sejarah dan nilai budaya tinggi.")
        intro = f"{topic} adalah destinasi wisata yang sangat menarik di Kabupaten Indramayu, Jawa Barat. {history} Tempat ini telah menjadi bagian penting dari kehidupan masyarakat lokal dan menawarkan pengalaman wisata yang unik bagi para pengunjung."
        paragraphs.append(intro)
        
        # Paragraph 2: Location and Access
        location = data.get('location', f"berlokasi di wilayah Indramayu dan dapat diakses dengan mudah menggunakan kendaraan pribadi atau transportasi umum")
        access = f"Secara geografis, {topic} {location}. Akses menuju lokasi ini cukup mudah dengan kondisi jalan yang baik dan tersedia berbagai pilihan transportasi. Pengunjung disarankan untuk datang pada pagi atau sore hari agar dapat menikmati suasana yang lebih nyaman dan mendapatkan pengalaman optimal."
        paragraphs.append(access)
        
        # Paragraph 3: Attractions and Cultural Significance
        attractions = data.get('attractions', f"berbagai kegiatan menarik dan fasilitas yang memadai untuk kenyamanan pengunjung")
        culture = data.get('culture', f"memiliki nilai budaya dan sejarah yang penting bagi masyarakat Indramayu")
        events = data.get('events', f"berbagai acara dan kegiatan yang diselenggarakan secara rutin")
        final = f"Di {topic}, pengunjung dapat menikmati {attractions}. Tempat ini juga {culture}. Selain itu, {events}, menjadikan lokasi ini tidak hanya sebagai tempat wisata tetapi juga sebagai pusat kegiatan budaya dan sosial masyarakat setempat."
        paragraphs.append(final)
        
        return "\n\n".join(paragraphs)
    
    def generate_detailed_answer_indramayu(self, topic: str, question: str) -> str:
        """Generate detailed answer in Bahasa Indramayu"""
        data = self.location_data.get(topic, {})
        
        if not data:
            return self.generate_generic_answer_indramayu(topic)
        
        # Build detailed 3-paragraph answer in Indramayu dialect
        paragraphs = []
        
        # Paragraph 1: Introduction and History in Indramayu dialect
        history_ind = data.get('history', f"{topic} iku salah siji panggon sing menarik nang Indramayu lan duwe sejarah sing penting")
        intro = f"{topic} iku destinasi wisata sing apik banget nang Kabupaten Indramayu, Jawa Barat. {history_ind}. Panggon iki wis dadi bagian penting saka urip masyarakat lokal lan nawakaken pengalaman wisata sing unik kanggo para pengunjung."
        paragraphs.append(intro)
        
        # Paragraph 2: Location and Access in Indramayu dialect  
        location_ind = data.get('location', f"ana nang wilayah Indramayu lan bisa digayuh kanthi gampang nganggo kendaraan pribadi utawa transportasi umum")
        access = f"Secara geografis, {topic} {location_ind}. Akses menyang lokasi iki cukup gampang kanthi kondisi dalan sing apik lan ana macem-macem pilihan transportasi. Pengunjung disaranaken teka nang esuk utawa sore ben bisa nikmati suasana sing luwih nyaman lan entuk pengalaman sing optimal."
        paragraphs.append(access)
        
        # Paragraph 3: Attractions and Cultural Significance in Indramayu dialect
        attractions_ind = data.get('attractions', f"macem-macem kegiatan menarik lan fasilitas sing cukup kanggo kenyamanan pengunjung")
        culture_ind = data.get('culture', f"duwe nilai budaya lan sejarah sing penting kanggo masyarakat Indramayu")
        events_ind = data.get('events', f"macem-macem acara lan kegiatan sing dianakaken sacara rutin")
        final = f"Nang {topic}, pengunjung bisa nikmati {attractions_ind}. Panggon iki uga {culture_ind}. Saliyane iku, {events_ind}, ndadekaken lokasi iki ora mung dadi papan wisata nanging uga dadi pusat kegiatan budaya lan sosial masyarakat setempat."
        paragraphs.append(final)
        
        return "\n\n".join(paragraphs)
    
    def generate_generic_answer_id(self, topic: str) -> str:
        """Generate generic but detailed answer in Bahasa Indonesia for topics without specific data"""
        paragraphs = [
            f"{topic} merupakan salah satu destinasi wisata yang menarik di Kabupaten Indramayu, Jawa Barat. Tempat ini memiliki daya tarik tersendiri yang menjadikannya layak untuk dikunjungi oleh wisatawan lokal maupun mancanegara. Dengan keunikan dan keindahan yang dimiliki, {topic} telah menjadi bagian penting dari kekayaan wisata Indramayu yang patut untuk dilestarikan dan dikembangkan.",
            
            f"Lokasi {topic} dapat diakses dengan mudah menggunakan berbagai jenis transportasi, baik kendaraan pribadi maupun transportasi umum. Kondisi jalan menuju lokasi ini umumnya dalam keadaan baik sehingga memudahkan perjalanan wisatawan. Pengunjung disarankan untuk mempersiapkan diri dengan baik sebelum berkunjung, termasuk mengecek kondisi cuaca dan membawa perlengkapan yang sesuai dengan aktivitas yang akan dilakukan.",
            
            f"Di {topic}, pengunjung dapat menikmati berbagai fasilitas dan aktivitas menarik yang telah disediakan untuk memaksimalkan pengalaman wisata. Tempat ini juga memiliki nilai budaya dan sejarah yang penting bagi masyarakat Indramayu, sehingga kunjungan ke sini tidak hanya memberikan hiburan tetapi juga edukasi. Berbagai event dan kegiatan rutin juga sering diselenggarakan di lokasi ini, menjadikannya sebagai pusat aktivitas sosial dan budaya yang hidup dan dinamis."
        ]
        
        return "\n\n".join(paragraphs)
    
    def generate_generic_answer_indramayu(self, topic: str) -> str:
        """Generate generic but detailed answer in Bahasa Indramayu for topics without specific data"""
        paragraphs = [
            f"{topic} iku salah siji destinasi wisata sing menarik nang Kabupaten Indramayu, Jawa Barat. Panggon iki duwe daya tarik dhewe sing ndadekaken layak kanggo dikunjungi dening wisatawan lokal utawa mancanegara. Kanthi keunikan lan kaindahan sing diduweni, {topic} wis dadi bagian penting saka kekayaan wisata Indramayu sing kudu dilestarikan lan dikembangaken.",
            
            f"Lokasi {topic} bisa digayuh kanthi gampang nganggo macem-macem jenis transportasi, baik kendaraan pribadi utawa transportasi umum. Kondisi dalan menyang lokasi iki umume nang keadaan apik dadi mempermudah perjalanan wisatawan. Pengunjung disaranaken kanggo nyiapaken awak kanthi apik sadurunge berkunjung, kalebu ngecek kondisi cuaca lan nggawa perlengkapan sing cocok karo aktivitas sing arep ditindakaken.",
            
            f"Nang {topic}, pengunjung bisa nikmati macem-macem fasilitas lan aktivitas menarik sing wis disediakaken kanggo memaksimalkan pengalaman wisata. Panggon iki uga duwe nilai budaya lan sejarah sing penting kanggo masyarakat Indramayu, dadi kunjungan mrene ora mung menehi hiburan nanging uga edukasi. Macem-macem event lan kegiatan rutin uga kerep dianakaken nang lokasi iki, ndadekaken dadi pusat aktivitas sosial lan budaya sing urip lan dinamis."
        ]
        
        return "\n\n".join(paragraphs)
    
    def generate_conversation_pair(self, topic: str) -> Tuple[Dict, Dict]:
        """Generate a pair of conversations (Indonesian and Indramayu) for a topic"""
        question = self.generate_question(topic)
        
        # Indonesian conversation
        id_conversation = {
            "conversations": [
                {
                    "role": "human", 
                    "content": question
                },
                {
                    "role": "assistant",
                    "content": self.generate_detailed_answer_id(topic, question)
                }
            ]
        }
        
        # Indramayu conversation  
        indramayu_conversation = {
            "conversations": [
                {
                    "role": "human",
                    "content": question
                },
                {
                    "role": "assistant", 
                    "content": self.generate_detailed_answer_indramayu(topic, question)
                }
            ]
        }
        
        return id_conversation, indramayu_conversation
    
    def generate_full_dataset(self) -> List[Dict]:
        """Generate complete dataset with conversations for all topics"""
        dataset = []
        
        for topic in self.topics:
            print(f"Generating conversations for: {topic}")
            id_conv, indramayu_conv = self.generate_conversation_pair(topic)
            dataset.append(id_conv)
            dataset.append(indramayu_conv)
        
        print(f"Generated {len(dataset)} conversations for {len(self.topics)} topics")
        return dataset
    
    def save_dataset(self, dataset: List[Dict], filename: str = "dataset.json"):
        """Save dataset to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, ensure_ascii=False, indent=2)
        print(f"Dataset saved to {filename}")

def main():
    print("Starting Indramayu Tourism Dataset Generation...")
    
    generator = IndramayuDatasetGenerator()
    
    if not generator.topics:
        print("Error: No topics found. Please check list-topik.txt file.")
        return
    
    print(f"Found {len(generator.topics)} topics to process")
    print("Topics:", generator.topics[:5], "..." if len(generator.topics) > 5 else "")
    
    dataset = generator.generate_full_dataset()
    generator.save_dataset(dataset)
    
    print("Dataset generation completed successfully!")
    print(f"Total conversations generated: {len(dataset)}")
    print(f"Each topic has 2 conversations (Indonesian + Indramayu)")

if __name__ == "__main__":
    main()