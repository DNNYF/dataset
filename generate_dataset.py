#!/usr/bin/env python3
"""
Script to generate JSON training data for conversational AI model.
Generates 2 objects per topic (same question, different language answers).
"""

import json
import re
from typing import List, Dict, Any

def parse_topics(file_path: str) -> List[str]:
    """Parse topics from the list-topik.txt file."""
    topics = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by lines and filter out empty lines and numbers
    lines = content.strip().split('\n')
    for line in lines:
        line = line.strip()
        # Skip empty lines and lines that are just numbers or "Berikut list wisatanya."
        if line and not line.isdigit() and line != "Berikut list wisatanya.":
            topics.append(line)
    
    return topics

def generate_question(topic: str) -> str:
    """Generate a question for the given topic."""
    # Remove numbers from the beginning if present
    clean_topic = re.sub(r'^\d+\.?\s*', '', topic).strip()
    
    # Different question patterns for variety
    question_patterns = [
        f"Bisakah Anda menceritakan tentang {clean_topic}?",
        f"Apa yang menarik dari {clean_topic}?",
        f"Bagaimana sejarah dan daya tarik {clean_topic}?",
        f"Ceritakan tentang {clean_topic} sebagai destinasi wisata.",
        f"Apa saja yang bisa dilakukan di {clean_topic}?"
    ]
    
    # Choose pattern based on topic characteristics
    if "pantai" in clean_topic.lower():
        return f"Ceritakan tentang keindahan dan daya tarik {clean_topic}."
    elif "museum" in clean_topic.lower() or "makam" in clean_topic.lower() or "situs" in clean_topic.lower():
        return f"Bagaimana sejarah dan nilai budaya {clean_topic}?"
    elif "waterpark" in clean_topic.lower() or "taman" in clean_topic.lower():
        return f"Apa saja fasilitas dan aktivitas yang ada di {clean_topic}?"
    elif "festival" in clean_topic.lower() or "upacara" in clean_topic.lower():
        return f"Ceritakan tentang tradisi dan makna {clean_topic}."
    elif "kuliner" in clean_topic.lower() or "makan" in clean_topic.lower():
        return f"Apa keistimewaan kuliner dan cita rasa {clean_topic}?"
    else:
        return f"Bisakah Anda menceritakan tentang {clean_topic}?"

def generate_indonesia_answer(topic: str) -> str:
    """Generate detailed answer in Bahasa Indonesia."""
    clean_topic = re.sub(r'^\d+\.?\s*', '', topic).strip()
    
    # Template for detailed answer structure
    if "pantai" in clean_topic.lower():
        return generate_beach_answer_id(clean_topic)
    elif "museum" in clean_topic.lower():
        return generate_museum_answer_id(clean_topic)
    elif "makam" in clean_topic.lower():
        return generate_tomb_answer_id(clean_topic)
    elif "waterpark" in clean_topic.lower():
        return generate_waterpark_answer_id(clean_topic)
    elif "festival" in clean_topic.lower() or "upacara" in clean_topic.lower():
        return generate_festival_answer_id(clean_topic)
    elif "kuliner" in clean_topic.lower() or "makan" in clean_topic.lower():
        return generate_culinary_answer_id(clean_topic)
    elif "taman" in clean_topic.lower():
        return generate_park_answer_id(clean_topic)
    elif "situ" in clean_topic.lower():
        return generate_lake_answer_id(clean_topic)
    elif "masjid" in clean_topic.lower():
        return generate_mosque_answer_id(clean_topic)
    elif "desa wisata" in clean_topic.lower():
        return generate_village_answer_id(clean_topic)
    else:
        return generate_general_answer_id(clean_topic)

def generate_indramayu_answer(topic: str) -> str:
    """Generate detailed answer in Bahasa Indramayu."""
    clean_topic = re.sub(r'^\d+\.?\s*', '', topic).strip()
    
    if "pantai" in clean_topic.lower():
        return generate_beach_answer_idr(clean_topic)
    elif "museum" in clean_topic.lower():
        return generate_museum_answer_idr(clean_topic)
    elif "makam" in clean_topic.lower():
        return generate_tomb_answer_idr(clean_topic)
    elif "waterpark" in clean_topic.lower():
        return generate_waterpark_answer_idr(clean_topic)
    elif "festival" in clean_topic.lower() or "upacara" in clean_topic.lower():
        return generate_festival_answer_idr(clean_topic)
    elif "kuliner" in clean_topic.lower() or "makan" in clean_topic.lower():
        return generate_culinary_answer_idr(clean_topic)
    elif "taman" in clean_topic.lower():
        return generate_park_answer_idr(clean_topic)
    elif "situ" in clean_topic.lower():
        return generate_lake_answer_idr(clean_topic)
    elif "masjid" in clean_topic.lower():
        return generate_mosque_answer_idr(clean_topic)
    elif "desa wisata" in clean_topic.lower():
        return generate_village_answer_idr(clean_topic)
    else:
        return generate_general_answer_idr(clean_topic)

# Indonesian answer generators
def generate_beach_answer_id(topic: str) -> str:
    return f"""{topic} merupakan salah satu destinasi pantai unggulan di Kabupaten Indramayu yang memiliki sejarah panjang sebagai wilayah pesisir utara Jawa. Pantai ini telah menjadi bagian dari kehidupan masyarakat lokal sejak zaman dahulu, dimana nelayan setempat menggunakan kawasan ini sebagai pangkalan utama untuk mencari ikan di Laut Jawa. Dengan perkembangan pariwisata modern, pantai ini kemudian dikembangkan menjadi objek wisata yang menawarkan keindahan alam pesisir yang memukau.

Secara geografis, {topic} terletak di wilayah pesisir utara Kabupaten Indramayu dan dapat diakses melalui berbagai jalur transportasi. Pengunjung dapat menggunakan kendaraan pribadi maupun transportasi umum dari pusat Kota Indramayu dengan perjalanan sekitar 30-45 menit. Jalur utama menuju pantai ini melalui jalan raya yang telah beraspal dengan baik, dan terdapat area parkir yang memadai untuk kendaraan wisatawan. Akses menuju pantai juga dilengkapi dengan penunjuk arah yang jelas sehingga memudahkan pengunjung pertama kali.

Aktivitas utama yang dapat dinikmati di {topic} sangat beragam, mulai dari berenang di air laut yang jernih, berjemur di hamparan pasir putih, hingga menikmati sunset yang spektakuler di sore hari. Pantai ini juga menyediakan berbagai fasilitas pendukung seperti warung makan yang menyajikan seafood segar hasil tangkapan nelayan lokal, area bermain anak, dan spot foto yang instagramable. Pengunjung juga dapat menyewa perahu untuk berkeliling laut atau memancing di area yang telah disediakan. Suasana pantai yang tenang dan angin laut yang sejuk menjadikan tempat ini ideal untuk relaksasi bersama keluarga atau teman-teman."""

def generate_museum_answer_id(topic: str) -> str:
    return f"""{topic} adalah salah satu ikon pelestarian sejarah dan budaya di Kabupaten Indramayu yang didirikan untuk melestarikan warisan leluhur dan memberikan edukasi kepada generasi muda. Museum ini memiliki latar belakang sejarah yang erat kaitannya dengan perkembangan peradaban di wilayah Indramayu, khususnya dalam bidang kebudayaan, sejarah, dan kehidupan sosial masyarakat. Pembangunan museum ini merupakan inisiatif pemerintah daerah untuk menjaga dan melestarikan artefak-artefak berharga yang mencerminkan identitas budaya lokal.

Museum ini berlokasi strategis di pusat Kota Indramayu dan mudah diakses menggunakan berbagai jenis transportasi. Pengunjung dapat menggunakan kendaraan pribadi, angkutan umum, atau ojek online untuk mencapai lokasi ini. Jam operasional museum biasanya dari pagi hingga sore hari dengan hari libur tertentu sesuai kebijakan pengelola. Fasilitas yang tersedia meliputi area parkir, ruang pameran ber-AC, toilet, dan area istirahat yang nyaman untuk pengunjung.

Koleksi utama {topic} mencakup berbagai artefak bersejarah, benda-benda budaya tradisional, dokumentasi sejarah, dan replika yang menggambarkan kehidupan masyarakat Indramayu dari masa ke masa. Pengunjung dapat melihat pameran tetap maupun pameran temporer yang menampilkan tema-tema khusus. Museum ini juga sering mengadakan kegiatan edukasi seperti workshop budaya, seminar sejarah, dan program kunjungan sekolah. Nilai budaya yang terkandung dalam museum ini sangat tinggi karena menjadi jendela untuk memahami perjalanan sejarah dan kekayaan budaya Indramayu yang perlu dilestarikan untuk generasi mendatang."""

def generate_tomb_answer_id(topic: str) -> str:
    return f"""{topic} merupakan situs bersejarah yang memiliki nilai spiritual dan budaya tinggi bagi masyarakat Indramayu. Makam ini menjadi tempat peristirahatan terakhir tokoh penting dalam sejarah daerah yang telah memberikan kontribusi besar bagi perkembangan Islam dan budaya lokal. Latar belakang sejarah makam ini tidak terlepas dari peranan tokoh yang dimakamkan dalam menyebarkan agama Islam dan membangun peradaban di wilayah Indramayu pada masa lampau. Keberadaan makam ini telah menjadi bagian integral dari warisan budaya yang harus dilestarikan.

Lokasi {topic} berada di area yang mudah dijangkau dari pusat kota dengan fasilitas akses jalan yang memadai. Pengunjung dapat menggunakan kendaraan pribadi atau transportasi umum untuk mencapai lokasi ini. Area sekitar makam telah dilengkapi dengan fasilitas pendukung seperti tempat parkir, toilet, dan area istirahat. Pengelolaan situs ini dilakukan dengan baik oleh pihak terkait dengan menjaga kebersihan dan kenyamanan pengunjung yang datang untuk berziarah atau sekadar belajar sejarah.

Aktivitas yang dapat dilakukan di {topic} meliputi ziarah spiritual, belajar sejarah, dan memahami nilai-nilai luhur yang ditinggalkan oleh tokoh yang dimakamkan. Pengunjung dapat melihat arsitektur makam yang mencerminkan gaya bangunan tradisional dengan ornamen-ornamen khas. Situs ini juga menjadi lokasi penelitian sejarah dan budaya bagi akademisi maupun pelajar. Nilai budaya dan historis yang terkandung sangat penting untuk memahami perkembangan Islam dan peradaban di Indramayu. Setiap tahunnya, makam ini juga menjadi lokasi penyelenggaraan acara-acara keagamaan dan budaya yang melibatkan masyarakat setempat."""

def generate_waterpark_answer_id(topic: str) -> str:
    return f"""{topic} adalah destinasi wisata air modern yang dikembangkan untuk memenuhi kebutuhan rekreasi keluarga di Kabupaten Indramayu. Waterpark ini dibangun dengan konsep taman air yang menyenangkan dan aman, menghadirkan wahana permainan air yang beragam untuk segala usia. Pengembangan waterpark ini merupakan respons terhadap meningkatnya kebutuhan masyarakat akan tempat rekreasi yang menyegarkan, terutama di daerah dengan iklim tropis seperti Indramayu. Konsep pembangunannya mengutamakan keselamatan pengunjung dengan standar internasional.

Waterpark ini berlokasi di area yang strategis dan mudah diakses dari berbagai penjuru Kabupaten Indramayu. Pengunjung dapat menggunakan kendaraan pribadi dengan memanfaatkan jalur utama yang telah beraspal baik, atau menggunakan transportasi umum yang tersedia. Fasilitas parkir yang luas telah disediakan untuk mengakomodasi kendaraan pengunjung. Area waterpark dilengkapi dengan berbagai fasilitas pendukung seperti kamar ganti, toilet, mushola, food court, dan area istirahat yang nyaman untuk keluarga.

Wahana utama di {topic} mencakup berbagai jenis kolam renang dengan kedalaman yang bervariasi, mulai dari kolam anak-anak yang dangkal hingga kolam dewasa dengan perosotan air yang menantang. Terdapat juga lazy river untuk bersantai, water slide dengan berbagai tingkat kesulitan, dan area bermain air untuk anak-anak yang dilengkapi dengan fitur-fitur menarik. Selain fasilitas air, waterpark ini juga menyediakan area gazebo untuk piknik keluarga dan berbagai permainan lainnya. Kegiatan yang dapat dinikmati meliputi berenang, bermain air, bersantai di pinggir kolam, dan menikmati berbagai makanan dan minuman di food court. Waterpark ini menjadi pilihan ideal untuk menghabiskan waktu berkualitas bersama keluarga sambil menikmati kesegaran air dan suasana yang menyenangkan."""

def generate_festival_answer_id(topic: str) -> str:
    return f"""{topic} merupakan tradisi budaya yang telah mengakar dalam kehidupan masyarakat Indramayu sejak turun-temurun. Festival atau upacara adat ini memiliki sejarah panjang yang berkaitan erat dengan sistem kepercayaan, tradisi maritim, dan siklus kehidupan masyarakat pesisir. Latar belakang historisnya berasal dari perpaduan antara tradisi Jawa kuno, pengaruh Islam, dan budaya maritim yang berkembang di wilayah pesisir utara Jawa. Acara ini biasanya diadakan pada waktu-waktu tertentu yang memiliki makna simbolis dan spiritual bagi masyarakat setempat.

Pelaksanaan {topic} biasanya berlangsung di lokasi-lokasi yang memiliki nilai sakral atau di pusat-pusat kebudayaan masyarakat Indramayu. Pengunjung dari luar daerah dapat menyaksikan acara ini dengan mengikuti jadwal pelaksanaan yang biasanya diumumkan melalui media lokal atau pemerintah daerah. Akses menuju lokasi acara relatif mudah dijangkau dengan transportasi umum maupun kendaraan pribadi. Panitia penyelenggara biasanya menyediakan area parkir dan fasilitas pendukung lainnya untuk kenyamanan pengunjung yang datang menyaksikan atau berpartisipasi dalam acara.

Rangkaian acara dalam {topic} mencakup berbagai aktivitas budaya seperti pertunjukan seni tradisional, prosesi ritual, pameran kerajinan lokal, dan berbagai kompetisi yang melibatkan masyarakat. Pengunjung dapat menyaksikan atraksi budaya yang autentik, mencicipi kuliner khas Indramayu, dan berinteraksi langsung dengan masyarakat lokal. Festival ini juga menjadi ajang promosi potensi daerah dan pelestarian budaya tradisional. Nilai budaya yang terkandung sangat kaya, meliputi nilai-nilai religius, kearifan lokal, solidaritas sosial, dan pelestarian lingkungan. Acara ini biasanya diadakan secara tahunan atau mengikuti kalender budaya tertentu, menjadikannya sebagai momen penting untuk memperkuat identitas budaya masyarakat Indramayu."""

def generate_culinary_answer_id(topic: str) -> str:
    return f"""{topic} merupakan representasi kekayaan kuliner tradisional Indramayu yang telah berkembang sejak berabad-abad lamanya. Sejarah kuliner ini tidak terlepas dari posisi geografis Indramayu sebagai daerah pesisir yang kaya akan hasil laut dan pertanian. Tradisi kuliner ini terbentuk dari perpaduan budaya Jawa, Sunda, dan pengaruh perdagangan maritim yang ramai di wilayah pesisir utara Jawa. Resep-resep tradisional ini diwariskan secara turun-temurun dengan tetap mempertahankan cita rasa autentik yang menjadi identitas kuliner Indramayu.

Pusat kuliner ini tersebar di berbagai lokasi strategis di Kabupaten Indramayu, mulai dari pasar tradisional, warung-warung pinggir jalan, hingga restoran yang lebih modern. Pengunjung dapat dengan mudah menemukan berbagai hidangan khas ini di pusat Kota Indramayu, area wisata, atau di desa-desa yang menjadi sentra produksi makanan tradisional. Akses menuju tempat-tempat kuliner ini sangat mudah dengan menggunakan kendaraan pribadi atau transportasi umum. Banyak pedagang yang buka dari pagi hingga malam, memberikan fleksibilitas bagi wisatawan untuk menikmati kuliner kapan saja.

Keunikan {topic} terletak pada penggunaan bahan-bahan lokal yang segar seperti hasil laut, sayuran tropis, dan rempah-rempah pilihan yang menghasilkan cita rasa yang khas dan menggugah selera. Proses pembuatan yang masih menggunakan teknik tradisional memberikan karakteristik tersendiri pada setiap hidangan. Pengunjung dapat menikmati berbagai varian hidangan dengan tingkat kepedasan dan kelezatan yang beragam, serta mempelajari proses pembuatan dari para pedagang yang ramah. Nilai budaya kuliner ini sangat tinggi karena mencerminkan kearifan lokal dalam mengolah bahan makanan dan menjadi media pelestarian tradisi. Selain itu, kuliner ini juga menjadi daya tarik wisata yang dapat meningkatkan ekonomi masyarakat lokal."""

def generate_park_answer_id(topic: str) -> str:
    return f"""{topic} adalah ruang terbuka hijau yang dikembangkan sebagai paru-paru kota dan tempat rekreasi keluarga di Kabupaten Indramayu. Taman ini dibangun dengan konsep yang menggabungkan fungsi ekologis, rekreasi, dan edukasi untuk memberikan manfaat maksimal bagi masyarakat. Latar belakang pembangunannya berasal dari kebutuhan akan ruang terbuka hijau di area perkotaan yang semakin padat, serta upaya pemerintah daerah untuk meningkatkan kualitas hidup masyarakat melalui penyediaan fasilitas rekreasi yang ramah lingkungan.

Lokasi {topic} berada di area yang strategis dan mudah diakses dari berbagai penjuru kota. Pengunjung dapat menggunakan kendaraan pribadi, sepeda motor, atau berjalan kaki jika berada di sekitar area taman. Fasilitas akses yang baik termasuk jalan yang beraspal, area parkir yang memadai, dan jalur pejalan kaki yang aman. Taman ini biasanya buka 24 jam dengan penerangan yang cukup untuk aktivitas malam hari, meskipun jam operasional fasilitas tertentu mungkin terbatas.

Fasilitas yang tersedia di {topic} sangat beragam dan dirancang untuk memenuhi kebutuhan rekreasi berbagai kalangan. Terdapat area bermain anak-anak dengan permainan yang aman dan menarik, jogging track untuk aktivitas olahraga, gazebo untuk istirahat dan berkumpul, serta area terbuka untuk berbagai kegiatan komunitas. Taman ini juga dilengkapi dengan toilet umum, kantin atau area jajanan, dan tempat duduk yang tersebar di berbagai sudut taman. Kegiatan yang dapat dilakukan meliputi olahraga pagi atau sore, bermain bersama anak-anak, piknik keluarga, fotografi, atau sekadar bersantai menikmati udara segar. Nilai ekologis taman ini sangat penting dalam menjaga keseimbangan lingkungan perkotaan dan memberikan ruang interaksi sosial yang sehat bagi masyarakat."""

def generate_lake_answer_id(topic: str) -> str:
    return f"""{topic} adalah danau alami yang memiliki peran penting dalam ekosistem dan kehidupan masyarakat di sekitar Kabupaten Indramayu. Secara historis, danau ini telah menjadi bagian dari sistem hidrologi regional yang mendukung kehidupan flora dan fauna lokal serta aktivitas masyarakat seperti perikanan dan pertanian. Pembentukan danau ini merupakan hasil dari proses geologis alami yang berlangsung ribuan tahun, menciptakan cekungan yang kemudian terisi air dari berbagai sumber seperti hujan, sungai, dan mata air bawah tanah.

Akses menuju {topic} dapat ditempuh melalui jalur darat dengan kondisi jalan yang cukup baik untuk kendaraan roda dua maupun roda empat. Pengunjung dapat menggunakan kendaraan pribadi atau menyewa transportasi lokal dari pusat kota. Perjalanan menuju danau ini menawarkan pemandangan perdesaan yang asri dengan hamparan sawah dan kebun yang hijau. Di sekitar danau tersedia fasilitas dasar seperti area parkir, warung makan sederhana, dan tempat istirahat untuk pengunjung.

Aktivitas yang dapat dinikmati di {topic} sangat beragam, mulai dari memancing di tepian danau, berperahu mengelilingi danau, hingga menikmati pemandangan alam yang menenangkan. Danau ini juga menjadi habitat berbagai jenis ikan air tawar dan burung-burung yang dapat diamati oleh pengunjung yang menyukai birdwatching. Suasana tenang dan udara segar di sekitar danau menjadikannya tempat ideal untuk meditasi atau sekadar bersantai melepas penat. Nilai ekologis danau ini sangat penting sebagai sumber air, habitat satwa, dan pengatur iklim mikro di wilayah sekitarnya. Masyarakat setempat juga sering menggunakan danau ini untuk kebutuhan sehari-hari dan sebagai sumber mata pencaharian melalui aktivitas perikanan."""

def generate_mosque_answer_id(topic: str) -> str:
    return f"""{topic} adalah salah satu bangunan keagamaan bersejarah yang memiliki peran sentral dalam kehidupan spiritual masyarakat Indramayu. Masjid ini dibangun pada masa perkembangan Islam di wilayah pesisir utara Jawa dan menjadi saksi perjalanan sejarah penyebaran agama Islam di daerah tersebut. Arsitektur masjid ini mencerminkan perpaduan gaya tradisional Jawa dengan pengaruh Islam yang khas, menunjukkan proses akulturasi budaya yang harmonis. Keberadaannya tidak hanya sebagai tempat ibadah, tetapi juga sebagai pusat kegiatan sosial dan pendidikan masyarakat.

Masjid ini berlokasi di area yang strategis dan mudah diakses dari berbagai penjuru kota. Pengunjung dapat menggunakan kendaraan pribadi atau transportasi umum untuk mencapai lokasi masjid. Fasilitas yang tersedia meliputi area parkir yang luas, tempat wudhu yang bersih, perpustakaan, dan ruang serbaguna untuk kegiatan kemasyarakatan. Masjid ini buka sepanjang waktu untuk kegiatan ibadah lima waktu, dengan jam khusus untuk kegiatan lain seperti pengajian dan pendidikan agama.

Kegiatan utama di {topic} meliputi ibadah shalat berjamaah, pengajian rutin, pendidikan agama untuk anak-anak dan dewasa, serta berbagai kegiatan sosial kemasyarakatan. Arsitektur masjid yang indah dengan ornamen-ornamen khas menjadi daya tarik tersendiri bagi pengunjung yang ingin mempelajari seni Islam tradisional. Masjid ini juga sering menjadi lokasi penyelenggaraan acara-acara keagamaan besar seperti peringatan hari-hari besar Islam. Nilai spiritual dan budaya yang terkandung sangat tinggi, menjadikan masjid ini sebagai simbol toleransi beragama dan pusat pengembangan nilai-nilai Islami dalam masyarakat. Peran masjid dalam memelihara tradisi keagamaan dan membangun karakter umat menjadikannya sebagai warisan budaya yang harus dilestarikan."""

def generate_village_answer_id(topic: str) -> str:
    return f"""{topic} merupakan konsep pengembangan pariwisata berbasis masyarakat yang mengangkat potensi lokal sebagai daya tarik utama. Desa wisata ini dikembangkan dengan tujuan memberdayakan masyarakat lokal sambil melestarikan budaya, tradisi, dan kearifan lokal yang telah turun-temurun. Konsep pembangunannya mengedepankan prinsip keberlanjutan dengan melibatkan partisipasi aktif masyarakat dalam pengelolaan dan pengembangan potensi wisata desa. Latar belakang historisnya berasal dari kehidupan masyarakat agraris dan nelayan yang memiliki tradisi budaya yang unik dan masih terjaga kelestariannya.

Desa wisata ini terletak di wilayah yang dapat diakses melalui jalur transportasi darat dengan pemandangan pedesaan yang asri. Pengunjung dapat menggunakan kendaraan pribadi atau transportasi umum untuk mencapai lokasi, dengan perjalanan yang menawarkan pengalaman melihat kehidupan pedesaan yang autentik. Fasilitas akomodasi tersedia dalam bentuk homestay yang dikelola oleh masyarakat setempat, memberikan pengalaman menginap yang berbeda dengan hotel konvensional. Fasilitas pendukung lainnya meliputi area parkir, toilet umum, dan pusat informasi wisata.

Aktivitas yang dapat dinikmati di {topic} sangat beragam dan memberikan pengalaman wisata yang mendalam. Pengunjung dapat berpartisipasi dalam kegiatan pertanian seperti menanam atau memanen padi, belajar membuat kerajinan tangan tradisional, menyaksikan pertunjukan seni budaya lokal, dan mencicipi kuliner khas desa yang diolah langsung oleh ibu-ibu setempat. Program edukasi tentang kearifan lokal, pengenalan flora dan fauna desa, serta workshop berbagai keterampilan tradisional juga tersedia untuk pengunjung. Nilai budaya yang dapat dipelajari meliputi gotong royong, kearifan dalam mengelola sumber daya alam, dan tradisi-tradisi yang masih dipraktikkan dalam kehidupan sehari-hari. Desa wisata ini juga mengadakan festival atau acara budaya tertentu yang melibatkan partisipasi pengunjung, memberikan pengalaman yang tak terlupakan dan pemahaman yang lebih dalam tentang kehidupan masyarakat pedesaan."""

def generate_general_answer_id(topic: str) -> str:
    return f"""{topic} adalah salah satu destinasi wisata menarik di Kabupaten Indramayu yang memiliki karakteristik unik dan nilai historis tersendiri. Tempat ini dikembangkan sebagai bagian dari upaya pemerintah daerah dan masyarakat untuk mempromosikan potensi pariwisata lokal yang beragam. Latar belakang sejarahnya terkait dengan perkembangan budaya dan peradaban masyarakat Indramayu yang kaya akan tradisi dan kearifan lokal. Keberadaan destinasi ini mencerminkan perpaduan antara nilai-nilai tradisional dengan perkembangan modern yang harmonis.

Lokasi {topic} berada di area yang strategis dan dapat diakses dengan mudah menggunakan berbagai jenis transportasi. Pengunjung dapat menggunakan kendaraan pribadi, transportasi umum, atau menyewa kendaraan lokal untuk mencapai tempat ini. Jalur akses yang tersedia umumnya dalam kondisi baik dengan penunjuk arah yang memadai. Fasilitas pendukung seperti area parkir, toilet, dan tempat istirahat tersedia untuk kenyamanan pengunjung. Jam operasional biasanya fleksibel, namun waktu terbaik untuk berkunjung adalah pada pagi atau sore hari untuk menikmati suasana yang lebih nyaman.

Daya tarik utama {topic} terletak pada keunikan dan keragaman aktivitas yang dapat dinikmati pengunjung. Tempat ini menawarkan pengalaman yang berbeda dari destinasi wisata pada umumnya, dengan nuansa lokal yang kental dan autentik. Pengunjung dapat menikmati berbagai aktivitas sesuai dengan karakter tempat ini, berinteraksi dengan masyarakat setempat, dan mempelajari nilai-nilai budaya yang terkandung di dalamnya. Nilai edukatif dan rekreatif yang ditawarkan sangat seimbang, menjadikan tempat ini cocok untuk berbagai kalangan pengunjung. Kontribusi destinasi ini terhadap pengembangan pariwisata daerah dan peningkatan ekonomi masyarakat lokal sangat signifikan, menjadikannya sebagai aset berharga yang perlu terus dikembangkan dan dilestarikan."""

# Indramayu language answer generators
def generate_beach_answer_idr(topic: str) -> str:
    return f"""{topic} iku salah siji pantai sing paling apik ning Kabupaten Indramayu. Pantai iki wis ana wiwit jaman biyen, dadi panggonan nelayan-nelayan lokal golek iwak ning Laut Jawa. Sejarahe dawa banget, soale pantai iki wis dadi bagian penting saka uripe wong Indramayu. Jaman saiki, pantai iki wis dikembangaken dadi objek wisata sing narik akeh wong saka macem-macem daerah kanggo main kene.

Panggonan {topic} iku gampang banget ditemokaken, soale ana ning pesisir lor Kabupaten Indramayu. Wong-wong sing arep mrene bisa nganggo motor, mobil, utawa angkutan umum saka tengah kutha Indramayu. Perjalanane mung butuh wektu 30-45 menit wae. Dalane wis bagus kabeh, wis diaspal apik, lan ana papan parkir sing akeh kanggo kendaraan para pengunjung. Aja kuwatir kesel golek dalan, soale wis ana papan-papan petunjuk arah sing jelas banget.

Ning {topic} iki, wong bisa nindakaken macem-macem kegiatan sing seru. Bisa adus ning segara, ngrebahaken awak ning pasir putih, utawa delok srengenge surup sing bagus banget. Ana warung-warung makan sing jual seafood seger hasil tangkapan nelayan lokal. Bocah-bocah uga bisa main ning area bermain sing wis disediakaken. Wong uga bisa nyewa prahu kanggo keliling segara utawa mancing ning tempat-tempat sing wis ditentokaken. Pantai iki tenang banget lan hawane adem, dadi cocok banget kanggo santai bareng kulawarga utawa kanca-kanca."""

def generate_museum_answer_idr(topic: str) -> str:
    return f"""{topic} iku museum sing penting banget kanggo njaga sejarah lan budaya wong Indramayu. Museum iki dibangun kanggo nguri-uri warisan leluhur lan menehi pengetahuan marang generasi mudha. Sejarahe museum iki ana hubungane karo perkembangan peradaban ning wilayah Indramayu, utamane ning bidang budaya, sejarah, lan kehidupan sosial masyarakat. Pemerintah daerah sing gawee inisiatif iki kanggo njaga barang-barang bersejarah sing berharga.

Museum iki dumunung ning tengah Kutha Indramayu lan gampang banget ditemokaken nganggo macem-macem transportasi. Wong bisa nganggo motor, mobil, angkutan umum, utawa ojek online kanggo tekan kene. Jam bukane biasane saka esuk nganti sore, lan ana hari libur tartamtu miturut kebijakan pengelola. Fasilitase lengkap banget, ana papan parkir, ruang pameran sing ber-AC, toilet, lan tempat istirahat sing nyaman kanggo para pengunjung.

Koleksi ning {topic} iki akeh banget, ana artefak bersejarah, barang-barang budaya tradisional, dokumentasi sejarah, lan replika-replika sing nggambaraken uripe wong Indramayu jaman biyen. Wong bisa delok pameran tetap utawa pameran sementara sing nampilaken tema-tema khusus. Museum iki uga kerep ngadakaken kegiatan edukasi kaya workshop budaya, seminar sejarah, lan program kunjungan sekolah. Nilai budayane dhuwur banget soale dadi jendela kanggo ngerti perjalanan sejarah lan kekayaan budaya Indramayu sing kudu dijaga kanggo generasi sing bakal teka."""

def generate_tomb_answer_idr(topic: str) -> str:
    return f"""{topic} iku makam bersejarah sing duwe nilai spiritual lan budaya dhuwur banget kanggo wong Indramayu. Makam iki dadi papan peristirahatan terakhir tokoh penting ning sejarah daerah sing wis menehi kontribusi gedhe kanggo perkembangan Islam lan budaya lokal. Sejarahe makam iki ora bisa dipisahaken saka peran tokoh sing dimakamaken ning nyebaraken agama Islam lan mbangun peradaban ning wilayah Indramayu jaman biyen. Keberadaane makam iki wis dadi bagian penting saka warisan budaya sing kudu dilestarikan.

Panggonan {topic} iku gampang ditemokaken saka tengah kutha, dalane uga wis apik. Wong bisa nganggo motor, mobil, utawa angkutan umum kanggo tekan kene. Area sakiwa tengene makam wis dilengkapi karo fasilitas pendukung kaya papan parkir, toilet, lan tempat istirahat. Pengelolaane apik banget, dijaga kebersihan lan kenyamanan kanggo para pengunjung sing teka ziarah utawa mung pengin sinau sejarah.

Kegiatan sing bisa ditindakaken ning {topic} iku ziarah spiritual, sinau sejarah, lan ngerti nilai-nilai luhur sing ditinggalaken dening tokoh sing dimakamaken. Para pengunjung bisa delok arsitektur makam sing nggambaraken gaya bangunan tradisional karo ornamen-ornamen khas. Situs iki uga dadi lokasi penelitian sejarah lan budaya kanggo para akademisi utawa pelajar. Nilai budaya lan historise penting banget kanggo ngerti perkembangan Islam lan peradaban ning Indramayu. Saben taun, makam iki uga dadi lokasi penyelenggaraan acara-acara keagamaan lan budaya sing nglibataken masyarakat setempat."""

def generate_waterpark_answer_idr(topic: str) -> str:
    return f"""{topic} iku tempat wisata air modern sing dibangun kanggo nyukupi kebutuhan rekreasi kulawarga ning Kabupaten Indramayu. Waterpark iki dibangun karo konsep taman air sing nyenengaken lan aman, nggawe wahana permainan air sing macem-macem kanggo kabeh umur. Pembangunan waterpark iki kanggo njawab kabutuhan masyarakat marang tempat rekreasi sing nyegeraken, utamane ning daerah karo iklim tropis kaya Indramayu. Konsep pembanguane ngutamakaken keselamatan pengunjung karo standar internasional.

Waterpark iki dumunung ning area strategis lan gampang ditemokaken saka macem-macem penjuru Kabupaten Indramayu. Para pengunjung bisa nganggo kendaraan pribadi nganggo jalur utama sing wis diaspal apik, utawa nganggo angkutan umum sing tersedia. Papan parkir sing akeh wis disediakaken kanggo kendaraan para pengunjung. Area waterpark dilengkapi karo macem-macem fasilitas pendukung kaya kamar ganti, toilet, mushola, food court, lan area istirahat sing nyaman kanggo kulawarga.

Wahana utama ning {topic} iku macem-macem jenis kolam renang karo kedalaman sing beda-beda, mulai saka kolam bocah-bocah sing cethek nganti kolam wong gedhe karo perosotan air sing menantang. Ana uga lazy river kanggo santai, water slide karo macem-macem tingkat kesulitan, lan area bermain air kanggo bocah-bocah sing dilengkapi karo fitur-fitur menarik. Selain fasilitas air, waterpark iki uga nyediakaken area gazebo kanggo piknik kulawarga lan macem-macem permainan liyane. Kegiatan sing bisa dinikmati kaya adus, main air, santai ning pinggir kolam, lan nikmati macem-macem panganan lan minuman ning food court. Waterpark iki dadi pilihan apik kanggo ngabisaken wektu karo kulawarga sambil nikmati kesegaran banyu lan suasana sing nyenengaken."""

def generate_festival_answer_idr(topic: str) -> str:
    return f"""{topic} iku tradisi budaya sing wis ngakar ning uripe masyarakat Indramayu wiwit turun-temurun. Festival utawa upacara adat iki duwe sejarah dawa sing ana hubungane karo sistem kepercayaan, tradisi maritim, lan siklus uripe masyarakat pesisir. Latar belakang historise asale saka perpaduan antara tradisi Jawa kuno, pengaruh Islam, lan budaya maritim sing berkembang ning wilayah pesisir lor Jawa. Acara iki biasane diadakaken ning wektu-wektu tartamtu sing duwe makna simbolis lan spiritual kanggo masyarakat setempat.

Pelaksanaan {topic} biasane ana ning lokasi-lokasi sing duwe nilai sakral utawa ning pusat-pusat kebudayaan masyarakat Indramayu. Para pengunjung saka luar daerah bisa ndelok acara iki karo ngikuti jadwal pelaksanaan sing biasane diumumaken lewat media lokal utawa pemerintah daerah. Akses menyang lokasi acara gampang banget ditemokaken karo transportasi umum utawa kendaraan pribadi. Panitia penyelenggara biasane nyediakaken area parkir lan fasilitas pendukung liyane kanggo kenyamanan para pengunjung sing teka ndelok utawa berpartisipasi ning acara.

Rangkaian acara ning {topic} iku akeh banget, ana macem-macem aktivitas budaya kaya pertunjukan seni tradisional, prosesi ritual, pameran kerajinan lokal, lan macem-macem kompetisi sing nglibataken masyarakat. Para pengunjung bisa ndelok atraksi budaya sing asli, nyicipi kuliner khas Indramayu, lan berinteraksi langsung karo masyarakat lokal. Festival iki uga dadi ajang promosi potensi daerah lan pelestarian budaya tradisional. Nilai budayane sugih banget, ana nilai-nilai religius, kearifan lokal, solidaritas sosial, lan pelestarian lingkungan. Acara iki biasane diadakaken tiap taun utawa ngikuti kalender budaya tartamtu, dadi momen penting kanggo nguataken identitas budaya masyarakat Indramayu."""

def generate_culinary_answer_idr(topic: str) -> str:
    return f"""{topic} iku perwakilan saka kekayaan kuliner tradisional Indramayu sing wis berkembang wiwit atusan taun kepungkur. Sejarah kuliner iki ora bisa dipisahaken saka posisi geografis Indramayu minangka daerah pesisir sing sugih karo hasil laut lan pertanian. Tradisi kuliner iki terbentuk saka perpaduan budaya Jawa, Sunda, lan pengaruh perdagangan maritim sing rame ning wilayah pesisir lor Jawa. Resep-resep tradisional iki diwarisaken secara turun-temurun karo tetep njaga rasa asli sing dadi identitas kuliner Indramayu.

Pusat kuliner iki nyebar ning macem-macem lokasi strategis ning Kabupaten Indramayu, mulai saka pasar tradisional, warung-warung pinggir dalan, nganti restoran sing luwih modern. Para pengunjung bisa gampang nemokaken macem-macem hidangan khas iki ning tengah Kutha Indramayu, area wisata, utawa ning desa-desa sing dadi sentra produksi panganan tradisional. Akses menyang tempat-tempat kuliner iki gampang banget nganggo kendaraan pribadi utawa transportasi umum. Akeh pedagang sing bukak saka esuk nganti bengi, menehi fleksibilitas kanggo para wisatawan nikmati kuliner kapan wae.

Keunikan {topic} iku ana ning nggunakake bahan-bahan lokal sing seger kaya hasil laut, sayuran tropis, lan rempah-rempah pilihan sing ngasilaken rasa khas lan nggugah selera. Proses pembuatan sing isih nganggo teknik tradisional menehi karakteristik dhewe ning saben hidangan. Para pengunjung bisa nikmati macem-macem varian hidangan karo tingkat kepedasan lan kelezatan sing beda-beda, serta sinau proses pembuatan saka para pedagang sing ramah. Nilai budaya kuliner iki dhuwur banget soale nggambaraken kearifan lokal ning ngolah bahan panganan lan dadi media pelestarian tradisi. Saliyane iku, kuliner iki uga dadi daya tarik wisata sing bisa ningkataken ekonomi masyarakat lokal."""

def generate_park_answer_idr(topic: str) -> str:
    return f"""{topic} iku ruang terbuka ijo sing dikembangaken minangka paru-paru kutha lan tempat rekreasi kulawarga ning Kabupaten Indramayu. Taman iki dibangun karo konsep sing nggabungaken fungsi ekologis, rekreasi, lan edukasi kanggo menehi manfaat maksimal kanggo masyarakat. Latar belakang pembangunanane asale saka kabutuhan marang ruang terbuka ijo ning area perkotaan sing tambah padet, serta upaya pemerintah daerah kanggo ningkataken kualitas urip masyarakat lewat penyediaan fasilitas rekreasi sing ramah lingkungan.

Lokasi {topic} ana ning area strategis lan gampang ditemokaken saka macem-macem penjuru kutha. Para pengunjung bisa nganggo kendaraan pribadi, sepeda motor, utawa mlaku-mlaku yen ana ning sakiwa tengene area taman. Fasilitas akses sing apik kalebu dalan sing diaspal, area parkir sing cukup, lan jalur pejalan kaki sing aman. Taman iki biasane buka 24 jam karo penerangan sing cukup kanggo aktivitas bengi, sanajan jam operasional fasilitas tartamtu mungkin terbatas.

Fasilitas sing ana ning {topic} iku macem-macem banget lan dirancang kanggo nyukupi kabutuhan rekreasi macem-macem kalangan. Ana area bermain bocah-bocah karo permainan sing aman lan menarik, jogging track kanggo aktivitas olahraga, gazebo kanggo istirahat lan kumpul-kumpul, serta area terbuka kanggo macem-macem kegiatan komunitas. Taman iki uga dilengkapi karo toilet umum, kantin utawa area jajanan, lan papan lungguh sing nyebar ning macem-macem sudut taman. Kegiatan sing bisa ditindakaken kaya olahraga esuk utawa sore, main bareng bocah-bocah, piknik kulawarga, fotografi, utawa mung santai nikmati hawa seger. Nilai ekologis taman iki penting banget kanggo njaga keseimbangan lingkungan perkotaan lan menehi ruang interaksi sosial sing sehat kanggo masyarakat."""

def generate_lake_answer_idr(topic: str) -> str:
    return f"""{topic} iku danau alami sing duwe peran penting ning ekosistem lan uripe masyarakat ning sakiwa tengene Kabupaten Indramayu. Secara historis, danau iki wis dadi bagian saka sistem hidrologi regional sing nyengkuyung uripe flora lan fauna lokal serta aktivitas masyarakat kaya perikanan lan pertanian. Pembentukan danau iki asale saka proses geologis alami sing berlangsung ewu taun, nggawe cekungan sing banjur diisi banyu saka macem-macem sumber kaya udan, kali, lan mata air bawah tanah.

Akses menyang {topic} bisa ditempuh lewat jalur darat karo kondisi dalan sing cukup apik kanggo kendaraan roda loro utawa papat. Para pengunjung bisa nganggo kendaraan pribadi utawa nyewa transportasi lokal saka tengah kutha. Perjalanan menyang danau iki nawaraken pemandangan perdesaan sing asri karo hamparan sawah lan kebon sing ijo. Ning sakiwa tengene danau ana fasilitas dasar kaya area parkir, warung makan sederhana, lan tempat istirahat kanggo para pengunjung.

Aktivitas sing bisa dinikmati ning {topic} iku macem-macem banget, mulai saka mancing ning tepian danau, naik prahu keliling danau, nganti nikmati pemandangan alam sing tenangaken. Danau iki uga dadi habitat macem-macem jenis iwak air tawar lan manuk-manuk sing bisa diamati dening para pengunjung sing seneng birdwatching. Suasana tenang lan hawa seger ning sakiwa tengene danau ndadekaken papan ideal kanggo meditasi utawa mung santai lepas penat. Nilai ekologis danau iki penting banget minangka sumber banyu, habitat satwa, lan pengatur iklim mikro ning wilayah sakiwa tengene. Masyarakat setempat uga kerep nganggo danau iki kanggo kabutuhan saben dina lan minangka sumber mata pencaharian lewat aktivitas perikanan."""

def generate_mosque_answer_idr(topic: str) -> str:
    return f"""{topic} iku salah siji bangunan keagamaan bersejarah sing duwe peran sentral ning urip spiritual masyarakat Indramayu. Masjid iki dibangun ning masa perkembangan Islam ning wilayah pesisir lor Jawa lan dadi saksi perjalanan sejarah penyebaran agama Islam ning daerah tersebut. Arsitektur masjid iki nggambaraken perpaduan gaya tradisional Jawa karo pengaruh Islam sing khas, nuduhaken proses akulturasi budaya sing harmonis. Keberadaane ora mung minangka tempat ibadah, nanging uga minangka pusat kegiatan sosial lan pendidikan masyarakat.

Masjid iki dumunung ning area strategis lan gampang ditemokaken saka macem-macem penjuru kutha. Para pengunjung bisa nganggo kendaraan pribadi utawa transportasi umum kanggo tekan lokasi masjid. Fasilitas sing tersedia kalebu area parkir sing akeh, papan wudhu sing resik, perpustakaan, lan ruang serbaguna kanggo kegiatan kemasyarakatan. Masjid iki buka sepanjang wektu kanggo kegiatan ibadah lima wektu, karo jam khusus kanggo kegiatan liya kaya pengajian lan pendidikan agama.

Kegiatan utama ning {topic} kalebu ibadah shalat berjamaah, pengajian rutin, pendidikan agama kanggo bocah-bocah lan wong gedhe, serta macem-macem kegiatan sosial kemasyarakatan. Arsitektur masjid sing apik karo ornamen-ornamen khas dadi daya tarik dhewe kanggo para pengunjung sing pengin sinau seni Islam tradisional. Masjid iki uga kerep dadi lokasi penyelenggaraan acara-acara keagamaan gedhe kaya peringatan hari-hari gedhe Islam. Nilai spiritual lan budaya sing ana dhuwur banget, ndadekaken masjid iki minangka simbol toleransi beragama lan pusat pengembangan nilai-nilai Islami ning masyarakat. Peran masjid ning njaga tradisi keagamaan lan mbangun karakter umat ndadekaken dheweke minangka warisan budaya sing kudu dilestarikan."""

def generate_village_answer_idr(topic: str) -> str:
    return f"""{topic} iku konsep pengembangan pariwisata berbasis masyarakat sing ngangkat potensi lokal minangka daya tarik utama. Desa wisata iki dikembangaken karo tujuan mberdayakaken masyarakat lokal sambil nglestarikan budaya, tradisi, lan kearifan lokal sing wis turun-temurun. Konsep pembangunanane ngutamakaken prinsip keberlanjutan karo nglibataken partisipasi aktif masyarakat ning pengelolaan lan pengembangan potensi wisata desa. Latar belakang historise asale saka uripe masyarakat agraris lan nelayan sing duwe tradisi budaya sing unik lan isih dijaga kelestariane.

Desa wisata iki dumunung ning wilayah sing bisa diakses lewat jalur transportasi darat karo pemandangan perdesaan sing asri. Para pengunjung bisa nganggo kendaraan pribadi utawa transportasi umum kanggo tekan lokasi, karo perjalanan sing nawaraken pengalaman ndelok uripe perdesaan sing asli. Fasilitas akomodasi tersedia ning bentuk homestay sing dikelola dening masyarakat setempat, menehi pengalaman nginep sing beda karo hotel konvensional. Fasilitas pendukung liyane kalebu area parkir, toilet umum, lan pusat informasi wisata.

Aktivitas sing bisa dinikmati ning {topic} iku macem-macem banget lan menehi pengalaman wisata sing jero. Para pengunjung bisa berpartisipasi ning kegiatan pertanian kaya tandur utawa panen pari, sinau gawe kerajinan tangan tradisional, ndelok pertunjukan seni budaya lokal, lan nyicipi kuliner khas desa sing diolah langsung dening ibu-ibu setempat. Program edukasi babagan kearifan lokal, pengenalan flora lan fauna desa, serta workshop macem-macem keterampilan tradisional uga tersedia kanggo para pengunjung. Nilai budaya sing bisa dipelajari kalebu gotong royong, kearifan ning ngelola sumber daya alam, lan tradisi-tradisi sing isih dipraktikaken ning urip saben dina. Desa wisata iki uga ngadakaken festival utawa acara budaya tartamtu sing nglibataken partisipasi para pengunjung, menehi pengalaman sing ora lali lan pemahaman sing luwih jero babagan uripe masyarakat perdesaan."""

def generate_general_answer_idr(topic: str) -> str:
    return f"""{topic} iku salah siji destinasi wisata menarik ning Kabupaten Indramayu sing duwe karakteristik unik lan nilai historis dhewe. Papan iki dikembangaken minangka bagian saka upaya pemerintah daerah lan masyarakat kanggo promosi potensi pariwisata lokal sing macem-macem. Latar belakang sejarahe ana hubungane karo perkembangan budaya lan peradaban masyarakat Indramayu sing sugih karo tradisi lan kearifan lokal. Keberadaan destinasi iki nggambaraken perpaduan antara nilai-nilai tradisional karo perkembangan modern sing harmonis.

Lokasi {topic} ana ning area strategis lan bisa diakses karo gampang nganggo macem-macem jenis transportasi. Para pengunjung bisa nganggo kendaraan pribadi, transportasi umum, utawa nyewa kendaraan lokal kanggo tekan papan iki. Jalur akses sing tersedia umume ning kondisi apik karo petunjuk arah sing memadai. Fasilitas pendukung kaya area parkir, toilet, lan tempat istirahat tersedia kanggo kenyamanan para pengunjung. Jam operasional biasane fleksibel, nanging wektu paling apik kanggo teka iku ning esuk utawa sore kanggo nikmati suasana sing luwih nyaman.

Daya tarik utama {topic} ana ning keunikan lan keragaman aktivitas sing bisa dinikmati para pengunjung. Papan iki nawaraken pengalaman sing beda saka destinasi wisata pada umumnya, karo nuansa lokal sing kental lan asli. Para pengunjung bisa nikmati macem-macem aktivitas miturut karakter papan iki, berinteraksi karo masyarakat setempat, lan sinau nilai-nilai budaya sing ana ning jerone. Nilai edukatif lan rekreatif sing ditawaraken seimbang banget, ndadekaken papan iki cocok kanggo macem-macem kalangan pengunjung. Kontribusi destinasi iki marang pengembangan pariwisata daerah lan peningkatan ekonomi masyarakat lokal signifikan banget, ndadekaken dheweke minangka aset berharga sing kudu terus dikembangaken lan dilestarikan."""

def main():
    """Main function to generate the dataset."""
    # Parse topics from file
    topics = parse_topics("/home/runner/work/dataset/dataset/list-topik.txt")
    
    print(f"Found {len(topics)} topics")
    print("First few topics:", topics[:5])
    
    # Generate dataset
    dataset = []
    
    for topic in topics:
        if not topic.strip():
            continue
            
        # Generate question
        question = generate_question(topic)
        
        # Generate answer in Bahasa Indonesia
        answer_id = generate_indonesia_answer(topic)
        
        # Generate answer in Bahasa Indramayu
        answer_idr = generate_indramayu_answer(topic)
        
        # Create two conversation objects
        conv_id = {
            "conversations": [
                {
                    "role": "human",
                    "content": question
                },
                {
                    "role": "assistant", 
                    "content": answer_id
                }
            ]
        }
        
        conv_idr = {
            "conversations": [
                {
                    "role": "human",
                    "content": question
                },
                {
                    "role": "assistant",
                    "content": answer_idr
                }
            ]
        }
        
        dataset.append(conv_id)
        dataset.append(conv_idr)
    
    # Save to file
    with open("/home/runner/work/dataset/dataset/new_dataset.json", 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(dataset)} conversation objects")
    print(f"Dataset saved to new_dataset.json")
    
    # Display sample
    print("\nSample conversation (Bahasa Indonesia):")
    print(json.dumps(dataset[0], ensure_ascii=False, indent=2))
    print("\nSample conversation (Bahasa Indramayu):")
    print(json.dumps(dataset[1], ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()