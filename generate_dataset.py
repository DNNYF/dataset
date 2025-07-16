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
                "history": "Pulau Biawak merupakan pulau kecil yang terletak di utara Pantai Karangsong. Nama 'Biawak' berasal dari populasi biawak liar yang menghuni pulau ini secara alami sejak ratusan tahun lalu. Pulau ini juga memiliki sejarah sebagai tempat perlindungan nelayan dari badai laut dan menjadi lokasi istirahat dalam perjalanan melaut yang jauh.",
                "location": "sekitar 40 km dari pusat kota Indramayu, dapat diakses melalui Pelabuhan Karangsong dengan perjalanan perahu selama 3-4 jam melewati perairan Laut Jawa yang tenang",
                "attractions": "pengamatan biawak komodo mini di habitat asli mereka, pantai berpasir putih dengan air laut jernih berwarna biru kehijauan, snorkeling untuk melihat terumbu karang, diving dengan visibility hingga 15 meter, dan menikmati sunset spektakuler di tengah laut lepas",
                "culture": "tempat yang dianggap sakral oleh masyarakat setempat dan sering dijadikan lokasi ritual tradisional nelayan untuk meminta keselamatan melaut, serta menjadi bagian dari cerita rakyat tentang penjaga laut",
                "events": "festival konservasi biawak yang diadakan setiap bulan Oktober, ekspedisi penelitian biawak bersama universitas, dan ritual sedekah laut oleh nelayan setempat"
            },
            "Pantai Karangsong": {
                "type": "pantai",
                "history": "Pantai Karangsong telah menjadi pelabuhan nelayan utama di Indramayu sejak era kolonial Belanda pada abad ke-19. Nama 'Karangsong' berasal dari kata 'karang' dan 'song' yang dalam bahasa Jawa berarti batu karang yang menyerupai rumah tradisional. Pantai ini juga menjadi saksi sejarah perjuangan kemerdekaan Indonesia sebagai jalur komunikasi pejuang.",
                "location": "terletak di Desa Karangsong, Kecamatan Indramayu, sekitar 35 km dari pusat kota Indramayu. Dapat dicapai melalui jalan raya Pantura dengan kondisi jalan beraspal mulus dan dilengkapi rambu petunjuk yang jelas",
                "attractions": "pelabuhan perikanan tradisional dengan ratusan perahu nelayan warna-warni, pasar ikan segar dengan berbagai jenis ikan laut, tempat pelelangan ikan (TPI) yang ramai setiap pagi, wisata kuliner seafood dengan menu andalan kepiting soka dan rajungan, serta pemandangan sunset yang memukau di dermaga nelayan",
                "culture": "pusat kehidupan nelayan tradisional dengan berbagai upacara adat laut seperti Nadran dan Sedekah Laut yang telah diwariskan turun-temurun. Masyarakat setempat juga melestarikan tradisi gotong royong dalam aktivitas melaut dan berbagi hasil tangkapan",
                "events": "upacara Nadran setiap bulan Suro dalam kalender Jawa, festival kuliner seafood setiap bulan Juli, pasar ikan harian yang paling ramai di pagi dan sore hari, serta pertunjukan kesenian Tarling di malam tertentu"
            },
            "Hutan Mangrove Karangsong": {
                "type": "hutan",
                "history": "Hutan Mangrove Karangsong merupakan kawasan konservasi yang dikembangkan sejak tahun 1990-an sebagai upaya pelestarian ekosistem pesisir dan pencegahan abrasi pantai. Awalnya area ini adalah lahan kosong yang kemudian ditanami mangrove melalui program rehabilitasi lingkungan yang melibatkan masyarakat setempat dan berbagai NGO.",
                "location": "berada di area pesisir Desa Karangsong, sekitar 2 km dari Pantai Karangsong. Dapat diakses melalui jalan raya Indramayu-Cirebon kemudian menuju pantai dengan jalan setapak yang telah diperbaiki dan dilengkapi papan petunjuk",
                "attractions": "jembatan kayu sepanjang 500 meter yang membentang di atas hutan mangrove, menara pengamatan setinggi 15 meter untuk bird watching, pengamatan berbagai spesies burung langka seperti blekok sawah dan kuntul, wisata edukasi ekosistem mangrove dengan pemandu lokal, spot fotografi alam yang Instagram-able, dan area camping ground yang nyaman",
                "culture": "dijadikan lokasi edukasi konservasi alam bagi masyarakat setempat dan menjadi simbol keberhasilan gotong royong dalam pelestarian lingkungan. Tempat ini juga menjadi penyangga kehidupan nelayan tradisional yang memahami pentingnya menjaga ekosistem laut",
                "events": "program penanaman mangrove setiap bulan yang melibatkan volunteer, tour edukasi konservasi untuk sekolah-sekolah, kegiatan birdwatching rutin setiap akhir pekan, dan workshop fotografi alam"
            },
            "Pantai Tirtamaya": {
                "type": "pantai", 
                "history": "Pantai Tirtamaya mulai dikembangkan sebagai destinasi wisata pada tahun 2000-an atas inisiatif masyarakat setempat yang ingin mengembangkan potensi wisata daerah. Nama 'Tirtamaya' berasal dari bahasa Sanskerta yang berarti 'air suci yang indah', mencerminkan harapan masyarakat akan pantai yang bersih dan lestari.",
                "location": "terletak di Desa Tirtamaya, Kecamatan Indramayu, sekitar 25 km dari pusat kota melalui jalan provinsi yang mudah dilalui. Terdapat area parkir luas dan akses yang ramah untuk semua kalangan termasuk penyandang disabilitas",
                "attractions": "pantai dengan ombak tenang yang cocok untuk berenang anak-anak, area bermain anak dengan wahana permainan yang aman, warung kuliner seafood dengan menu andalan ikan bakar dan kerang hijau, gazebo-gazebo untuk bersantai keluarga, dan banana boat untuk wisata air yang menyenangkan",
                "culture": "menjadi tempat rekreasi favorit keluarga dari berbagai daerah dan sering dijadikan lokasi acara syukuran, pernikahan outdoor, dan gathering masyarakat setempat. Pantai ini juga menjadi tempat pembelajaran bagi anak-anak tentang kehidupan laut",
                "events": "festival pantai bersih setiap bulan dengan partisipasi masyarakat luas, kompetisi memancing untuk umum setiap minggu, pertunjukan seni budaya lokal seperti Tari Topeng dan musik Tarling di akhir pekan, serta pasar kuliner malam di area pantai"
            },
            "Masjid Agung Indramayu": {
                "type": "masjid",
                "history": "Masjid Agung Indramayu dibangun pada abad ke-15 oleh Sultan Wiralodra sebagai pusat kegiatan keagamaan Islam di wilayah Indramayu. Arsitekturnya memadukan gaya Jawa tradisional dengan unsur Arab, mencerminkan akulturasi budaya dalam penyebaran Islam. Masjid ini telah mengalami beberapa kali renovasi namun tetap mempertahankan nilai historis dan arsitektur aslinya.",
                "location": "berada di jantung kota Indramayu, tepatnya di Jalan Jenderal Sudirman No. 1, sangat mudah diakses dengan berbagai transportasi umum seperti angkot, ojek, dan bus kota. Lokasi strategis ini membuatnya menjadi landmark utama kota Indramayu",
                "attractions": "arsitektur klasik dengan ornamen ukiran kayu Jawa yang indah, mihrab berornamen kaligrafi Arab yang megah, kubah utama berdiameter 12 meter dengan detail yang menawan, halaman luas yang dapat menampung ribuan jamaah, museum mini sejarah Islam Indramayu, dan perpustakaan dengan koleksi kitab-kitab klasik",
                "culture": "pusat kegiatan keagamaan dan sosial masyarakat Indramayu yang menjadi tempat berkumpulnya berbagai lapisan masyarakat. Masjid ini juga menjadi tempat pengajian akbar, diskusi keagamaan, dan pusat koordinasi kegiatan sosial keagamaan di wilayah Indramayu",
                "events": "shalat berjamaah Idul Fitri dan Idul Adha yang dihadiri ribuan jamaah, pengajian akbar setiap Jumat sore dengan penceramah ternama, kajian rutin setiap malam setelah shalat Maghrib, dan perayaan Maulid Nabi yang meriah"
            },
            "Makam Raden Arya Wiralodra": {
                "type": "makam",
                "history": "Makam Raden Arya Wiralodra adalah tempat peristirahatan terakhir pendiri Kabupaten Indramayu pada abad ke-15. Beliau adalah putra Sultan Cirebon yang ditugaskan untuk membuka wilayah baru dan menyebarkan agama Islam. Raden Arya Wiralodra dikenal sebagai sosok yang bijaksana, adil, dan sangat peduli dengan rakyatnya, sehingga dihormati hingga kini.",
                "location": "terletak di kompleks pemakaman Panjunan, Kelurahan Panjunan, Kecamatan Indramayu, sekitar 3 km dari pusat kota. Lokasi ini mudah diakses dengan kendaraan roda dua maupun roda empat dan tersedia area parkir yang memadai",
                "attractions": "makam berarsitektur Jawa kuno dengan cungkup kayu jati berukir indah, halaman luas dengan pohon-pohon tua yang rindang berusia ratusan tahun, museum mini sejarah Indramayu dengan koleksi artefak bersejarah, dan area taman yang asri untuk kontemplasi",
                "culture": "tempat ziarah dan spiritual yang sangat dihormati masyarakat Indramayu dan sekitarnya. Banyak peziarah yang datang untuk meminta berkah, doa untuk kesuksesan, dan pembelajaran spiritual. Tempat ini juga menjadi simbol kepemimpinan yang adil dan bijaksana",
                "events": "haul Raden Arya Wiralodra setiap tanggal wafatnya dengan prosesi tradisional Jawa, ziarah massal saat bulan Ramadan dan menjelang Idul Fitri, upacara tradisional Jawa seperti selametan dan doa bersama, serta kegiatan dakwah dan pengajian"
            },
            "Tugu Mangga": {
                "type": "tugu",
                "history": "Tugu Mangga dibangun sebagai simbol kebanggaan Indramayu yang terkenal dengan Mangga Gedong Gincu berkualitas premium yang telah mendapat pengakuan internasional. Tugu ini diresmikan pada tahun 2005 oleh Bupati Indramayu sebagai landmark kota dan penanda identitas daerah yang kuat akan komoditas unggulan mangga.",
                "location": "terletak di pusat kota Indramayu, tepatnya di persimpangan Jalan Jenderal Sudirman dan Jalan Letjen Suwondo, yang merupakan jalan utama menghubungkan berbagai wilayah kabupaten. Lokasi strategis ini membuatnya mudah ditemukan dan menjadi meeting point populer",
                "attractions": "tugu setinggi 15 meter berbentuk mangga raksasa dengan detail yang realistis dan cat berwarna emas mengkilap, taman kota dengan berbagai tanaman hias dan bunga warna-warni, area kuliner malam hari dengan berbagai menu lokal dan modern, serta spot foto favorit wisatawan dan keluarga",
                "culture": "menjadi identitas kota Indramayu dan simbol kejayaan pertanian mangga yang telah mengharumkan nama daerah hingga mancanegara. Tugu ini juga menjadi kebanggaan petani mangga lokal dan simbol kemakmuran dari sektor pertanian",
                "events": "Festival Mangga Gedong Gincu setiap bulan Juli-Agustus dengan berbagai kompetisi dan pameran, pameran produk lokal UMKM setiap akhir pekan, pertunjukan budaya tradisional seperti Wayang Kulit dan Tari Topeng, serta car free day setiap minggu pagi"
            },
            "Festival Mangga Gedong Gincu (event tahunan)": {
                "type": "festival",
                "history": "Festival Mangga Gedong Gincu pertama kali diadakan pada tahun 2008 sebagai upaya promosi mangga unggulan Indramayu yang telah mendapat sertifikat Indikasi Geografis dari Kementerian Hukum dan HAM. Festival ini lahir dari inisiatif petani mangga dan pemerintah daerah untuk mengangkat harkat dan martabat petani serta memperkenalkan keunggulan mangga Indramayu ke dunia.",
                "location": "diselenggarakan di berbagai lokasi strategis di Indramayu, dengan pusat acara di Alun-alun Puspawangi dan area Tugu Mangga. Event juga tersebar di kebun-kebun mangga milik petani untuk memberikan pengalaman wisata agro yang autentik",
                "attractions": "pameran mangga dari ratusan petani dengan berbagai varietas unggulan, lomba makan mangga dengan hadiah menarik, demo pengolahan produk mangga menjadi berbagai makanan dan minuman, bazaar kuliner khas Indramayu dengan menu berbahan dasar mangga, workshop pembuatan olahan mangga, dan tur kebun mangga guided",
                "culture": "merayakan hasil panen mangga terbaik dan melestarikan tradisi pertanian yang sudah turun-temurun selama puluhan generasi di masyarakat Indramayu. Festival ini juga menjadi ajang silaturahmi petani dan apresiasi terhadap kerja keras mereka dalam menghasilkan mangga berkualitas dunia",
                "events": "diadakan setiap bulan Juli-Agustus selama musim panen mangga puncak, meliputi parade float bertema mangga, kompetisi fotografi dengan tema agrowisata, pertunjukan seni budaya lokal, pameran teknologi pertanian modern, dan festival kuliner dengan chef ternama"
            },
            "Upacara Adat Nadran (event tahunan)": {
                "type": "upacara",
                "history": "Upacara Nadran adalah tradisi turun-temurun masyarakat nelayan Indramayu yang telah berlangsung selama berabad-abad, diperkirakan sudah ada sejak abad ke-16. Nadran berasal dari kata 'nadzar' yang berarti janji atau sumpah kepada Yang Maha Kuasa. Tradisi ini merupakan warisan budaya yang menggabungkan nilai-nilai Islam dengan kearifan lokal masyarakat pesisir.",
                "location": "dilaksanakan di berbagai pantai di Indramayu, terutama Pantai Karangsong sebagai pusat utama, dengan prosesi menuju laut lepas menggunakan ratusan perahu tradisional yang dihias dengan bendera warna-warni. Acara juga melibatkan desa-desa pesisir lainnya",
                "attractions": "prosesi larung sesaji ke laut dengan perahu hias yang spektakuler, pertunjukan kesenian tradisional seperti Tari Topeng Indramayu yang memukau, pertunjukan Wayang Kulit semalam suntuk, musik tradisional Tarling yang merdu, parade budaya dengan kostum tradisional, dan pameran hasil laut",
                "culture": "tradisi syukur nelayan atas hasil tangkapan ikan dan permohonan keselamatan dalam melaut yang mencerminkan hubungan harmonis manusia dengan alam. Upacara ini juga menjadi media pelestarian nilai-nilai gotong royong, kebersamaan, dan spiritualitas masyarakat pesisir",
                "events": "diadakan setiap bulan Suro (Muharram) dalam penanggalan Jawa dengan rangkaian acara selama satu minggu penuh, meliputi berbagai ritual keagamaan, pertunjukan seni, pasar rakyat, dan festival kuliner seafood tradisional"
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