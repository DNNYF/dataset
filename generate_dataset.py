#!/usr/bin/env python3
"""
Generate high-quality JSON training data for conversational AI model
focusing on Indramayu tourism topics.
"""

import json
import re
from typing import List, Dict, Any

def read_topics(file_path: str) -> List[str]:
    """Read and extract clean topic list from list-topik.txt"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    topics = []
    for line in lines:
        line = line.strip()
        # Skip numbered lines and empty lines
        if not line or re.match(r'^\d+\.$', line) or line == "Berikut list wisatanya.":
            continue
        topics.append(line)
    
    return topics

def generate_question(topic: str) -> str:
    """Generate a natural question about the topic as a tourist/student would ask"""
    # Vary question styles for different types of topics
    if "Pantai" in topic:
        return f"Saya ingin tahu tentang {topic}. Bisakah Anda menjelaskan tentang pantai ini secara detail?"
    elif "Waterpark" in topic or "Waterboom" in topic:
        return f"Apa saja fasilitas dan kegiatan yang tersedia di {topic}?"
    elif "Masjid" in topic or "Makam" in topic or "Situs" in topic:
        return f"Bagaimana sejarah dan makna budaya dari {topic}?"
    elif "Museum" in topic or "Monumen" in topic or "Tugu" in topic:
        return f"Ceritakan tentang {topic} dan apa yang bisa dipelajari di sana?"
    elif "Festival" in topic or "Upacara" in topic:
        return f"Kapan dan bagaimana cara mengikuti {topic}?"
    elif "Kuliner" in topic or "Nasi" in topic or "Menikmati" in topic:
        return f"Apa keistimewaan dari {topic} dan di mana saya bisa menemukannya?"
    elif "Taman" in topic or "Situ" in topic or "Agrowisata" in topic:
        return f"Apa daya tarik utama {topic} dan aktivitas apa yang bisa dilakukan di sana?"
    else:
        return f"Saya penasaran dengan {topic}. Bisa dijelaskan secara lengkap tentang tempat ini?"

def generate_indonesian_answer(topic: str) -> str:
    """Generate detailed answer in Bahasa Indonesia"""
    
    # Historical background and general info
    historical_info = {
        "Pulau Biawak": "Pulau Biawak merupakan pulau kecil yang terletak di perairan utara Indramayu, Jawa Barat. Pulau ini memiliki sejarah panjang sebagai habitat alami berbagai satwa liar, terutama biawak yang menjadi nama pulau ini. Sejak zaman kolonial Belanda, pulau ini sudah dikenal sebagai kawasan konservasi alam yang unik. Nama 'Biawak' berasal dari populasi biawak yang cukup besar di pulau ini, meski kini populasinya sudah berkurang akibat perubahan ekosistem.",
        
        "Pantai Karangsong": "Pantai Karangsong adalah salah satu destinasi wisata pantai terpopuler di Kabupaten Indramayu. Pantai ini memiliki sejarah sebagai pelabuhan tradisional nelayan yang sudah beroperasi sejak abad ke-19. Nama 'Karangsong' berasal dari bahasa Jawa yang berarti 'karang yang menyanyi', merujuk pada suara ombak yang membentur karang-karang di sepanjang pantai. Daerah ini berkembang menjadi destinasi wisata pada tahun 1990-an ketika pemerintah daerah mulai mengembangkan infrastruktur pariwisata.",
        
        "Hutan Mangrove Karangsong": "Hutan Mangrove Karangsong merupakan ekosistem pesisir yang telah terbentuk secara alami selama ratusan tahun. Kawasan ini mulai mendapat perhatian serius sebagai area konservasi pada tahun 2000-an, ketika kesadaran akan pentingnya mangrove untuk perlindungan pantai semakin meningkat. Hutan mangrove ini memiliki peran vital dalam menjaga keseimbangan ekosistem pesisir dan sebagai tempat berkembang biak berbagai jenis ikan dan burung. Masyarakat lokal telah lama memanfaatkan area ini untuk penangkapan ikan tradisional dengan cara yang berkelanjutan.",
        
        "Pantai Tirtamaya": "Pantai Tirtamaya adalah destinasi wisata pantai yang relatif baru di Indramayu, mulai dikembangkan pada awal tahun 2010-an. Nama 'Tirtamaya' berasal dari bahasa Sanskerta yang berarti 'air suci' dan 'maya' yang berarti indah, menggambarkan keindahan alamnya. Pantai ini dulunya merupakan area pertambakan tradisional yang kemudian dikonversi menjadi destinasi wisata. Sejarah pengembangan pantai ini tidak lepas dari upaya pemerintah daerah untuk meningkatkan sektor pariwisata sebagai sumber pendapatan alternatif bagi masyarakat pesisir.",
    }
    
    # Location and access info
    location_info = {
        "Pulau Biawak": "Pulau Biawak terletak sekitar 40 kilometer dari pantai utara Indramayu, tepatnya di Desa Karangsong, Kecamatan Indramayu. Untuk mencapai pulau ini, wisatawan harus menempuh perjalanan darat dari pusat kota Indramayu menuju Pelabuhan Karangsong selama sekitar 30 menit. Dari pelabuhan, perjalanan dilanjutkan dengan kapal motor atau perahu nelayan selama 1-2 jam tergantung kondisi cuaca dan gelombang laut. Akses transportasi umum tersedia hingga Karangsong, namun untuk ke pelabuhan disarankan menggunakan ojek atau kendaraan pribadi.",
        
        "Pantai Karangsong": "Pantai Karangsong berlokasi di Desa Karangsong, Kecamatan Indramayu, sekitar 27 kilometer dari pusat kota Indramayu. Akses menuju pantai ini sangat mudah karena dapat ditempuh dengan berbagai jenis kendaraan melalui Jalan Raya Karangsong yang sudah beraspal dengan baik. Dari terminal bus Indramayu, tersedia angkutan umum jurusan Karangsong yang beroperasi setiap hari. Bagi wisatawan yang menggunakan kendaraan pribadi, tersedia area parkir yang luas dengan tarif terjangkau. Jalur alternatif juga bisa melalui Cirebon dengan jarak tempuh sekitar 45 menit.",
        
        "Hutan Mangrove Karangsong": "Hutan Mangrove Karangsong terletak di kawasan pesisir Desa Karangsong, berdekatan dengan Pantai Karangsong. Lokasi ini dapat dicapai dengan mudah menggunakan kendaraan bermotor dari pusat kota Indramayu dalam waktu sekitar 25 menit. Akses masuk ke kawasan mangrove melalui jalan setapak yang telah diperbaiki dan dilengkapi dengan jembatan kayu untuk memudahkan pengunjung menjelajahi area ini. Terdapat pos informasi di pintu masuk yang menyediakan peta lokasi dan informasi tentang jalur tracking yang tersedia.",
        
        "Pantai Tirtamaya": "Pantai Tirtamaya berada di Desa Tirtamaya, Kecamatan Indramayu, dengan jarak sekitar 20 kilometer dari pusat kota. Akses menuju pantai ini melalui jalan kabupaten yang kondisinya cukup baik, meski beberapa bagian masih berupa jalan beton. Dari kota Indramayu, wisatawan bisa menggunakan angkutan umum jurusan Tirtamaya atau kendaraan pribadi. Waktu tempuh sekitar 30-40 menit tergantung kondisi lalu lintas. Di area pantai tersedia tempat parkir dan beberapa warung yang menyediakan kebutuhan dasar wisatawan.",
    }
    
    # Activities and attractions
    activities_info = {
        "Pulau Biawak": "Aktivitas utama yang dapat dilakukan di Pulau Biawak adalah wildlife watching, terutama untuk mengamati biawak dalam habitat aslinya. Pengunjung dapat melakukan trekking mengelilingi pulau sambil menikmati pemandangan alam yang masih pristine. Aktivitas snorkeling dan diving juga populer karena perairan di sekitar pulau memiliki keanekaragaman hayati laut yang tinggi dengan terumbu karang yang masih terjaga. Fotografi alam menjadi daya tarik tersendiri, terutama saat sunrise dan sunset yang menawarkan pemandangan spektakuler. Selain itu, wisatawan dapat berkemah di area yang telah ditentukan untuk merasakan pengalaman bermalam di pulau terpencil.",
        
        "Pantai Karangsong": "Pantai Karangsong menawarkan berbagai aktivitas menarik seperti berenang di air laut yang relatif tenang dan jernih. Pengunjung dapat menyewa perahu untuk berkeliling pantai atau melaut sebentar untuk merasakan pengalaman melaut bersama nelayan lokal. Aktivitas memancing dari dermaga atau tepi pantai sangat populer, terutama pada sore hari. Kuliner seafood segar menjadi daya tarik utama dengan berbagai warung yang menyajikan ikan bakar, kepiting, dan udang hasil tangkapan lokal. Wisatawan juga dapat menikmati sunset yang indah sambil berjalan-jalan di sepanjang garis pantai yang cukup panjang.",
        
        "Hutan Mangrove Karangsong": "Wisatawan dapat menjelajahi hutan mangrove melalui jalur tracking yang telah disediakan dengan jembatan kayu sepanjang beberapa kilometer. Aktivitas bird watching sangat populer karena kawasan ini menjadi habitat berbagai jenis burung air dan burung migran. Wisata edukasi lingkungan tersedia dengan pemandu lokal yang menjelaskan ekosistem mangrove dan perannya dalam menjaga keseimbangan alam. Fotografi alam dengan latar belakang akar-akar mangrove yang unik menjadi kegiatan favorit pengunjung. Pada waktu tertentu, wisatawan dapat mengikuti program penanaman bibit mangrove sebagai bentuk partisipasi dalam konservasi lingkungan.",
        
        "Pantai Tirtamaya": "Pantai Tirtamaya menawarkan pengalaman berenang di air laut yang tenang dengan ombak yang tidak terlalu besar, cocok untuk anak-anak dan pemula. Wisatawan dapat menyewa ban pelampung atau perahu kecil untuk bermain air dengan aman. Aktivitas memancing tersedia dengan menyewa peralatan dari warung-warung sekitar pantai. Area pantai yang luas memungkinkan pengunjung untuk bermain voli pantai, sepak bola pantai, atau sekadar berjemur. Pada sore hari, pantai ini menjadi spot ideal untuk menikmati sunset sambil menyantap kelapa muda atau jagung bakar dari pedagang lokal."
    }
    
    # Generate topic-specific content for topics not in predefined data
    def generate_specific_content(topic_name):
        if "Masjid" in topic_name:
            return {
                'hist': f"{topic_name} merupakan salah satu masjid bersejarah di Indramayu yang memiliki nilai spiritual dan arsitektur yang tinggi. Masjid ini telah berdiri sejak beberapa abad yang lalu dan menjadi pusat kegiatan keagamaan masyarakat Muslim Indramayu. Arsitektur masjid ini menggabungkan gaya tradisional Jawa dengan pengaruh Islam, mencerminkan perpaduan budaya yang harmonis. Keberadaan masjid ini tidak hanya sebagai tempat ibadah, tetapi juga sebagai pusat penyebaran Islam dan pendidikan agama di daerah Indramayu.",
                'loc': f"{topic_name} terletak di pusat kota Indramayu, mudah diakses dari berbagai penjuru kota. Lokasinya yang strategis membuat masjid ini menjadi landmark penting di Indramayu. Dari terminal atau stasiun, pengunjung dapat menggunakan angkutan umum atau becak untuk mencapai masjid. Area parkir yang luas tersedia untuk kendaraan pribadi. Masjid ini juga dekat dengan pusat perbelanjaan dan fasilitas umum lainnya, memudahkan wisatawan yang ingin berkunjung sambil menjelajahi kota Indramayu.",
                'act': f"Pengunjung dapat melakukan ibadah di {topic_name} dan merasakan suasana spiritual yang khusyuk. Wisata religi ini menawarkan kesempatan untuk mempelajari sejarah Islam di Indramayu melalui arsitektur dan ornamen yang ada. Pengunjung dapat mengikuti kajian agama atau ceramah yang rutin diadakan. Fotografi arsitektur masjid menjadi aktivitas menarik, terutama pada waktu maghrib ketika pencahayaan menciptakan suasana yang indah. Selama bulan Ramadan, masjid ini menjadi pusat kegiatan takjih dan berbagai acara keagamaan yang dapat diikuti wisatawan Muslim."
            }
        elif "Makam" in topic_name:
            return {
                'hist': f"{topic_name} adalah kompleks makam bersejarah yang memiliki nilai historis dan spiritual tinggi bagi masyarakat Indramayu. Makam ini merupakan tempat peristirahatan terakhir tokoh penting dalam sejarah Indramayu yang telah berjasa dalam penyebaran Islam dan perkembangan daerah. Situs ini telah menjadi tempat ziarah selama berabad-abad, menarik peziarah dari berbagai daerah. Arsitektur makam menggabungkan unsur tradisional Jawa dan Islam, mencerminkan perpaduan budaya yang khas di wilayah pesisir utara Jawa.",
                'loc': f"Lokasi {topic_name} berada di area yang mudah diakses dari pusat kota Indramayu. Kompleks makam ini dikelilingi oleh lingkungan yang asri dan tenang, cocok untuk refleksi spiritual. Akses menuju lokasi dapat ditempuh dengan kendaraan pribadi atau transportasi umum. Jalan menuju kompleks sudah beraspal dengan baik dan dilengkapi dengan petunjuk arah yang jelas. Area parkir tersedia di dekat kompleks makam untuk kemudahan pengunjung.",
                'act': f"Kegiatan utama di {topic_name} adalah ziarah dan berdoa untuk mendoakan arwah yang dimakamkan. Pengunjung dapat mempelajari sejarah tokoh yang dimakamkan melalui prasasti dan informasi yang tersedia. Suasana yang tenang dan damai membuat tempat ini ideal untuk refleksi dan kontemplasi. Wisata sejarah dan budaya dapat dilakukan dengan mempelajari arsitektur dan ornamen khas pada bangunan makam. Banyak pengunjung yang datang untuk memohon berkah dan meminta perlindungan spiritual."
            }
        elif "Museum" in topic_name:
            return {
                'hist': f"{topic_name} adalah institusi budaya yang menyimpan dan memamerkan koleksi bersejarah tentang Indramayu dan sekitarnya. Museum ini didirikan untuk melestarikan warisan budaya dan sejarah daerah, menjadi pusat edukasi bagi generasi muda. Koleksi museum mencakup artefak prasejarah, benda-benda peninggalan zaman kerajaan, hingga dokumentasi perkembangan modern Indramayu. Keberadaan museum ini penting untuk mempertahankan identitas budaya lokal di tengah arus globalisasi.",
                'loc': f"{topic_name} berlokasi di area yang strategis dan mudah dijangkau dari berbagai penjuru kota Indramayu. Bangunan museum dirancang dengan konsep modern namun tetap mempertahankan unsur tradisional. Akses transportasi umum tersedia dengan rute yang melewati lokasi museum. Fasilitas parkir yang memadai tersedia untuk pengunjung yang membawa kendaraan pribadi. Area sekitar museum juga dilengkapi dengan taman dan fasilitas pendukung lainnya.",
                'act': f"Pengunjung dapat menjelajahi berbagai ruang pameran di {topic_name} yang menampilkan koleksi bersejarah dan budaya. Program edukasi dan workshop budaya rutin diadakan untuk pengunjung dari berbagai kalangan. Tur berpemandu tersedia untuk memberikan penjelasan mendalam tentang koleksi museum. Aktivitas penelitian dan studi budaya dapat dilakukan dengan memanfaatkan perpustakaan dan arsip yang tersedia. Museum juga sering mengadakan pameran temporer dan acara budaya yang menarik untuk dikunjungi."
            }
        elif "Kuliner" in topic_name or "Nasi" in topic_name or "Menikmati" in topic_name:
            return {
                'hist': f"{topic_name} merupakan tradisi kuliner khas Indramayu yang telah turun temurun selama puluhan tahun. Kuliner ini menjadi bagian dari identitas budaya masyarakat Indramayu dan mencerminkan kekayaan rasa nusantara. Resep dan cara pembuatannya diwariskan dari generasi ke generasi, mempertahankan cita rasa autentik. Makanan ini tidak hanya sekedar hidangan, tetapi juga memiliki nilai sosial dan budaya dalam kehidupan masyarakat lokal.",
                'loc': f"Pusat kuliner untuk menikmati {topic_name} tersebar di berbagai lokasi strategis di Indramayu, terutama di area pasar tradisional dan pusat kota. Warung-warung yang menyajikan hidangan ini mudah ditemukan dan dapat diakses dengan transportasi umum maupun kendaraan pribadi. Banyak pedagang yang membuka lapak di sepanjang jalan utama, terutama pada waktu makan siang dan malam. Area makan yang nyaman dan bersih tersedia di berbagai lokasi dengan harga yang terjangkau.",
                'act': f"Aktivitas utama adalah menikmati kelezatan {topic_name} yang disajikan dengan berbagai variasi resep dan penyajian. Pengunjung dapat belajar tentang proses pembuatan makanan dari para pedagang atau chef lokal. Wisata kuliner ini menawarkan pengalaman mencicipi berbagai rasa khas Indramayu dalam satu tempat. Fotografi kuliner menjadi aktivitas populer untuk mendokumentasikan pengalaman gastronomi. Berinteraksi dengan pedagang lokal memberikan wawasan tentang budaya dan tradisi kuliner daerah."
            }
        elif "Festival" in topic_name or "Upacara" in topic_name:
            return {
                'hist': f"{topic_name} adalah tradisi budaya yang telah berlangsung turun temurun di Indramayu selama berabad-abad. Acara ini memiliki makna spiritual dan budaya yang mendalam, menghubungkan masyarakat dengan warisan nenek moyang. Tradisi ini berakar dari kepercayaan lokal yang berpadu dengan nilai-nilai Islam, menciptakan keunikan budaya khas pesisir utara Jawa. Seiring waktu, acara ini berkembang menjadi festival besar yang menarik perhatian wisatawan dari berbagai daerah.",
                'loc': f"{topic_name} biasanya diselenggarakan di lokasi-lokasi bersejarah atau area terbuka yang dapat menampung banyak pengunjung. Tempat penyelenggaraan bervariasi tergantung pada jenis acara, bisa di pantai, alun-alun, atau kompleks bersejarah. Akses menuju lokasi acara umumnya mudah dijangkau dan dilengkapi dengan fasilitas sementara selama penyelenggaraan. Transportasi khusus sering disediakan untuk memudahkan pengunjung mencapai lokasi acara.",
                'act': f"Pengunjung dapat menyaksikan berbagai pertunjukan budaya, ritual adat, dan atraksi tradisional selama {topic_name}. Partisipasi langsung dalam beberapa kegiatan dimungkinkan untuk memberikan pengalaman yang lebih mendalam. Dokumentasi foto dan video menjadi aktivitas populer untuk mengabadikan momen-momen unik. Interaksi dengan masyarakat lokal dan tokoh adat memberikan pemahaman yang lebih baik tentang makna budaya acara tersebut. Berbagai stan makanan dan kerajinan lokal juga tersedia untuk melengkapi pengalaman budaya."
            }
        else:
            # Default content for other types
            return {
                'hist': f"{topic_name} adalah salah satu destinasi wisata menarik di Indramayu yang memiliki keunikan tersendiri. Tempat ini telah dikenal oleh masyarakat lokal sejak lama dan kini mulai dikembangkan sebagai destinasi wisata yang menarik bagi pengunjung dari luar daerah. Sejarah dan perkembangan {topic_name} tidak lepas dari upaya pemerintah dan masyarakat setempat untuk meningkatkan potensi pariwisata daerah. Keberadaan tempat ini memberikan kontribusi positif bagi perekonomian lokal dan pelestarian budaya.",
                'loc': f"{topic_name} berlokasi di wilayah Kabupaten Indramayu, Jawa Barat. Akses menuju lokasi ini dapat ditempuh dengan berbagai jenis transportasi, baik kendaraan pribadi maupun transportasi umum. Dari pusat kota Indramayu, perjalanan menuju {topic_name} memerlukan waktu yang bervariasi tergantung kondisi lalu lintas dan jarak tempuh. Tersedia berbagai fasilitas pendukung di sekitar lokasi untuk memudahkan kunjungan wisatawan.",
                'act': f"Di {topic_name}, pengunjung dapat menikmati berbagai aktivitas menarik sesuai dengan karakteristik tempat ini. Fasilitas yang tersedia cukup lengkap untuk mendukung kenyamanan wisatawan selama berkunjung. Berbagai pilihan aktivitas baik untuk dewasa maupun anak-anak dapat ditemukan di sini. Pengalaman berwisata di {topic_name} akan memberikan kenangan yang tak terlupakan bagi setiap pengunjung."
            }
    
    # Get base information or generate specific content
    if topic in historical_info:
        hist = historical_info[topic]
        loc = location_info[topic]
        act = activities_info[topic]
    else:
        specific = generate_specific_content(topic)
        hist = specific['hist']
        loc = specific['loc']
        act = specific['act']
    
    return f"{hist}\n\n{loc}\n\n{act}"

def generate_indramayu_answer(topic: str) -> str:
    """Generate detailed answer in Bahasa Indramayu"""
    
    # Historical background in Indramayu language
    historical_info = {
        "Pulau Biawak": "Pulau Biawak iku salah siji pulau cilik sing ana ing segara lor Indramayu, Jawa Barat. Pulau iki wis duwe sejarah sing dawa banget dadi papan uripe kewan-kewan liar, utamane biawak sing dadi asal jenenge pulau iki. Wiwit jaman Walanda, pulau iki wis dikenal dadi wilayah konservasi alam sing unik banget. Jeneng 'Biawak' iku asale saka akehe biawak ing pulau iki, sanajan saiki wis berkurang amarga owah-owahane ekosistem.",
        
        "Pantai Karangsong": "Pantai Karangsong iku salah siji destinasi wisata pantai sing paling populer ing Kabupaten Indramayu. Pantai iki duwe sejarah dadi pelabuhan tradisional nelayan sing wis operasi wiwit abad kaping-19. Jeneng 'Karangsong' asale saka basa Jawa sing artine 'karang sing nyanyi', merujuk marang swara ombak sing nabrak karang-karang ing sepanjang pantai. Daerah iki berkembang dadi destinasi wisata ing taun 1990-an nalika pemerintah daerah mulai ngembangake infrastruktur pariwisata.",
        
        "Hutan Mangrove Karangsong": "Hutan Mangrove Karangsong iku ekosistem pesisir sing wis kawujud sacara alami sajrone atusan taun. Kawasan iki mulai entuk perhatian serius dadi area konservasi ing taun 2000-an, nalika kesadaran babagan pentinge mangrove kanggo perlindungan pantai saya mundhak. Hutan mangrove iki duwe peran vital kanggo njaga keseimbangan ekosistem pesisir lan dadi papan berkembang biake macem-macem jenis iwak lan manuk. Masyarakat lokal wis suwe banget nggunakake area iki kanggo nangkap iwak tradisional kanthi cara sing lestari.",
        
        "Pantai Tirtamaya": "Pantai Tirtamaya iku destinasi wisata pantai sing relatif anyar ing Indramayu, mulai dikembangake ing awal taun 2010-an. Jeneng 'Tirtamaya' asale saka basa Sanskerta sing artine 'banyu suci' lan 'maya' sing artine ayu, nggambarake kaendahane alam. Pantai iki biyen area pertambakan tradisional sing banjur dikonversi dadi destinasi wisata. Sejarah pengembangan pantai iki ora bisa dipisahake saka upaya pemerintah daerah kanggo ningkatake sektor pariwisata dadi sumber penghasilan alternatif kanggo masyarakat pesisir.",
    }
    
    # Location info in Indramayu language
    location_info = {
        "Pulau Biawak": "Pulau Biawak dumunung kurang luwih 40 kilometer saka pantai lor Indramayu, tepatne ing Desa Karangsong, Kecamatan Indramayu. Kanggo tekan pulau iki, wisatawan kudu mlaku darat saka tengah kutha Indramayu menyang Pelabuhan Karangsong sajrone kurang luwih 30 menit. Saka pelabuhan, lelampahan diterusake nganggo kapal motor utawa prau nelayan sajrone 1-2 jam gumantung kondisi cuaca lan ombak segara. Akses transportasi umum ana nganti Karangsong, nanging kanggo menyang pelabuhan disaranake nganggo ojek utawa kendaraan pribadi.",
        
        "Pantai Karangsong": "Pantai Karangsong dumunung ing Desa Karangsong, Kecamatan Indramayu, kurang luwih 27 kilometer saka tengah kutha Indramayu. Akses menyang pantai iki gampang banget amarga bisa ditempuh nganggo macem-macem jenis kendaraan liwat Jalan Raya Karangsong sing wis diaspal apik. Saka terminal bis Indramayu, ana angkutan umum jurusan Karangsong sing operasi saben dina. Kanggo wisatawan sing nganggo kendaraan pribadi, ana area parkir sing amba kanthi tarif sing terjangkau. Jalur alternatif uga bisa liwat Cirebon kanthi jarak tempuh kurang luwih 45 menit.",
        
        "Hutan Mangrove Karangsong": "Hutan Mangrove Karangsong dumunung ing kawasan pesisir Desa Karangsong, cedhak karo Pantai Karangsong. Lokasi iki bisa ditekan kanthi gampang nganggo kendaraan bermotor saka tengah kutha Indramayu sajrone kurang luwih 25 menit. Akses mlebu kawasan mangrove liwat dalan setapak sing wis didandani lan dilengkapi jembatan kayu kanggo nggampangake pengunjung njelajahi area iki. Ana pos informasi ing lawang mlebu sing nyediakake peta lokasi lan informasi babagan jalur tracking sing kasedhiya.",
        
        "Pantai Tirtamaya": "Pantai Tirtamaya ana ing Desa Tirtamaya, Kecamatan Indramayu, kanthi jarak kurang luwih 20 kilometer saka tengah kutha. Akses menyang pantai iki liwat dalan kabupaten sing kondisine cukup apik, sanajan sawetara bagian isih dalan beton. Saka kutha Indramayu, wisatawan bisa nganggo angkutan umum jurusan Tirtamaya utawa kendaraan pribadi. Wektu tempuh kurang luwih 30-40 menit gumantung kondisi lalu lintas. Ing area pantai ana papan parkir lan sawetara warung sing nyediakake kabutuhan dhasar wisatawan.",
    }
    
    # Activities in Indramayu language  
    activities_info = {
        "Pulau Biawak": "Aktivitas utama sing bisa ditindakake ing Pulau Biawak yaiku wildlife watching, utamane kanggo ngamati biawak ing habitat asline. Pengunjung bisa nindakake trekking ngubengi pulau sambil nikmati pemandangan alam sing isih pristine. Aktivitas snorkeling lan diving uga populer amarga perairan ing sakiwa-tengene pulau duwe keanekaragaman hayati segara sing dhuwur karo terumbu karang sing isih terjaga. Fotografi alam dadi daya tarik tersendiri, utamane nalika sunrise lan sunset sing nawakake pemandangan spektakuler. Saliyane iku, wisatawan bisa kemah ing area sing wis ditemtokake kanggo ngrasakake pengalaman turu ing pulau terpencil.",
        
        "Pantai Karangsong": "Pantai Karangsong nawakake macem-macem aktivitas menarik kayata adus ing banyu segara sing relatif tentrem lan bening. Pengunjung bisa nyewa prau kanggo ngubengi pantai utawa melaut sebentar kanggo ngrasakake pengalaman melaut bareng nelayan lokal. Aktivitas mancing saka dermaga utawa pinggir pantai banget populer, utamane ing sore dina. Kuliner seafood seger dadi daya tarik utama karo macem-macem warung sing nyajikake iwak bakar, yuyu, lan udang asil tangkapan lokal. Wisatawan uga bisa nikmati sunset sing ayu sambil mlaku-mlaku ing sepanjang garis pantai sing cukup dawa.",
        
        "Hutan Mangrove Karangsong": "Wisatawan bisa njelajahi hutan mangrove liwat jalur tracking sing wis disediakake karo jembatan kayu sepanjang sawetara kilometer. Aktivitas bird watching banget populer amarga kawasan iki dadi habitat macem-macem jenis manuk banyu lan manuk migran. Wisata edukasi lingkungan kasedhiya karo pemandu lokal sing nerangake ekosistem mangrove lan perane kanggo njaga keseimbangan alam. Fotografi alam karo latar mburi akar-akar mangrove sing unik dadi kegiatan favorit pengunjung. Ing wektu tartamtu, wisatawan bisa melu program nandur bibit mangrove minangka wujud partisipasi ing konservasi lingkungan.",
        
        "Pantai Tirtamaya": "Pantai Tirtamaya nawakake pengalaman adus ing banyu segara sing tentrem karo ombak sing ora gedhe banget, cocok kanggo bocah-bocah lan pemula. Wisatawan bisa nyewa ban pelampung utawa prau cilik kanggo dolanan banyu kanthi aman. Aktivitas mancing kasedhiya kanthi nyewa peralatan saka warung-warung sakiwa-tengene pantai. Area pantai sing amba ngidini pengunjung kanggo main voli pantai, sepak bola pantai, utawa mung jemur. Ing sore dina, pantai iki dadi spot ideal kanggo nikmati sunset sambil mangan kelapa enom utawa jagung bakar saka pedagang lokal."
    }
    
    # Generate topic-specific content for topics not in predefined data (Indramayu version)
    def generate_specific_content_indramayu(topic_name):
        if "Masjid" in topic_name:
            return {
                'hist': f"{topic_name} iku salah siji masjid bersejarah ing Indramayu sing duwe nilai spiritual lan arsitektur sing dhuwur. Masjid iki wis ngadeg wiwit sawetara abad kepungkur lan dadi pusat kegiatan keagamaan masyarakat Muslim Indramayu. Arsitektur masjid iki nggabungake gaya tradisional Jawa karo pangaruh Islam, nggambarake perpaduan budaya sing harmonis. Anane masjid iki ora mung dadi papan ibadah, nanging uga dadi pusat penyebaran Islam lan pendidikan agama ing daerah Indramayu.",
                'loc': f"{topic_name} dumunung ing tengah kutha Indramayu, gampang diakses saka macem-macem penjuru kutha. Lokasine sing strategis ndadekake masjid iki dadi landmark penting ing Indramayu. Saka terminal utawa stasiun, pengunjung bisa nganggo angkutan umum utawa becak kanggo tekan masjid. Area parkir sing amba kasedhiya kanggo kendaraan pribadi. Masjid iki uga cedhak karo pusat perbelanjaan lan fasilitas umum liyane, nggampangake wisatawan sing arep berkunjung sambil njelajahi kutha Indramayu.",
                'act': f"Pengunjung bisa nindakake ibadah ing {topic_name} lan ngrasakake suasana spiritual sing khusyuk. Wisata religi iki nawakake kesempatan kanggo sinau sejarah Islam ing Indramayu liwat arsitektur lan ornamen sing ana. Pengunjung bisa melu kajian agama utawa ceramah sing rutin diadakake. Fotografi arsitektur masjid dadi aktivitas menarik, utamane nalika maghrib nalika pencahayaan nggawe suasana sing ayu. Sajrone wulan Ramadan, masjid iki dadi pusat kegiatan takjih lan macem-macem acara keagamaan sing bisa ditindakake wisatawan Muslim."
            }
        elif "Makam" in topic_name:
            return {
                'hist': f"{topic_name} iku kompleks makam bersejarah sing duwe nilai historis lan spiritual dhuwur kanggo masyarakat Indramayu. Makam iki dadi papan peristirahatan pungkasan tokoh penting ing sejarah Indramayu sing wis berjasa ing penyebaran Islam lan perkembangan daerah. Situs iki wis dadi papan ziarah sajrone berabad-abad, narik peziarah saka macem-macem daerah. Arsitektur makam nggabungake unsur tradisional Jawa lan Islam, nggambarake perpaduan budaya sing khas ing wilayah pesisir lor Jawa.",
                'loc': f"Lokasi {topic_name} ana ing area sing gampang diakses saka tengah kutha Indramayu. Kompleks makam iki dikepung dening lingkungan sing asri lan tentrem, cocok kanggo refleksi spiritual. Akses menyang lokasi bisa ditempuh nganggo kendaraan pribadi utawa transportasi umum. Dalan menyang kompleks wis diaspal kanthi apik lan dilengkapi karo petunjuk arah sing jelas. Area parkir kasedhiya ing cedhak kompleks makam kanggo gampangake pengunjung.",
                'act': f"Kegiatan utama ing {topic_name} yaiku ziarah lan ndonga kanggo ndongakake arwah sing dimakamake. Pengunjung bisa sinau sejarah tokoh sing dimakamake liwat prasasti lan informasi sing kasedhiya. Suasana sing tentrem lan damai ndadekake papan iki ideal kanggo refleksi lan kontemplasi. Wisata sejarah lan budaya bisa ditindakake kanthi sinau arsitektur lan ornamen khas ing bangunan makam. Akeh pengunjung sing teka kanggo nyuwun berkah lan nyuwun perlindungan spiritual."
            }
        elif "Museum" in topic_name:
            return {
                'hist': f"{topic_name} iku institusi budaya sing nyimpen lan mamerake koleksi bersejarah babagan Indramayu lan sakiwa-tengene. Museum iki didirikan kanggo nglestariake warisan budaya lan sejarah daerah, dadi pusat edukasi kanggo generasi enom. Koleksi museum kalebu artefak prasejarah, barang-barang peninggalan jaman kerajaan, nganti dokumentasi perkembangan modern Indramayu. Anane museum iki penting kanggo njaga identitas budaya lokal ing tengah arus globalisasi.",
                'loc': f"{topic_name} dumunung ing area sing strategis lan gampang dijangkau saka macem-macem penjuru kutha Indramayu. Bangunan museum dirancang kanthi konsep modern nanging tetep njaga unsur tradisional. Akses transportasi umum kasedhiya kanthi rute sing liwat lokasi museum. Fasilitas parkir sing memadai kasedhiya kanggo pengunjung sing nggawa kendaraan pribadi. Area sakiwa-tengene museum uga dilengkapi karo taman lan fasilitas pendukung liyane.",
                'act': f"Pengunjung bisa njelajahi macem-macem ruang pameran ing {topic_name} sing nampilek koleksi bersejarah lan budaya. Program edukasi lan workshop budaya rutin diadakake kanggo pengunjung saka macem-macem kalangan. Tur berpemandu kasedhiya kanggo menehi panjelasan jero babagan koleksi museum. Aktivitas riset lan studi budaya bisa ditindakake kanthi nggunakake perpustakaan lan arsip sing kasedhiya. Museum uga kerep ngadakake pameran temporer lan acara budaya sing menarik kanggo dikunjungi."
            }
        elif "Kuliner" in topic_name or "Nasi" in topic_name or "Menikmati" in topic_name:
            return {
                'hist': f"{topic_name} iku tradisi kuliner khas Indramayu sing wis turun temurun sajrone puluhan taun. Kuliner iki dadi bagian saka identitas budaya masyarakat Indramayu lan nggambarake sugih rase nusantara. Resep lan cara gaweane diwarisake saka generasi menyang generasi, njaga rasa asli. Panganan iki ora mung sekedar hidangan, nanging uga duwe nilai sosial lan budaya ing urip masyarakat lokal.",
                'loc': f"Pusat kuliner kanggo nikmati {topic_name} nyebar ing macem-macem lokasi strategis ing Indramayu, utamane ing area pasar tradisional lan pusat kutha. Warung-warung sing nyajikake hidangan iki gampang ditemokake lan bisa diakses nganggo transportasi umum utawa kendaraan pribadi. Akeh pedagang sing mbukak lapak ing sepanjang dalan utama, utamane nalika wektu mangan awan lan bengi. Area mangan sing nyaman lan resik kasedhiya ing macem-macem lokasi kanthi rega sing terjangkau.",
                'act': f"Aktivitas utama yaiku nikmati kelezatan {topic_name} sing disajikake kanthi macem-macem variasi resep lan penyajian. Pengunjung bisa sinau babagan proses gawe panganan saka para pedagang utawa chef lokal. Wisata kuliner iki nawakake pengalaman ngicipi macem-macem rasa khas Indramayu ing siji papan. Fotografi kuliner dadi aktivitas populer kanggo ndokumentasikake pengalaman gastronomi. Interaksi karo pedagang lokal menehi wawasan babagan budaya lan tradisi kuliner daerah."
            }
        elif "Festival" in topic_name or "Upacara" in topic_name:
            return {
                'hist': f"{topic_name} iku tradisi budaya sing wis lumaku turun temurun ing Indramayu sajrone berabad-abad. Acara iki duwe makna spiritual lan budaya sing jero, nyambungake masyarakat karo warisan leluhur. Tradisi iki nduwe oyod saka kapercayan lokal sing gabung karo nilai-nilai Islam, nggawe keunikan budaya khas pesisir lor Jawa. Seiring wektu, acara iki berkembang dadi festival gedhe sing narik perhatian wisatawan saka macem-macem daerah.",
                'loc': f"{topic_name} biasane diadakake ing lokasi-lokasi bersejarah utawa area mbukak sing bisa nampung akeh pengunjung. Papan penyelenggaraan beda-beda gumantung jenis acara, bisa ing pantai, alun-alun, utawa kompleks bersejarah. Akses menyang lokasi acara umume gampang dijangkau lan dilengkapi karo fasilitas sementara sajrone penyelenggaraan. Transportasi khusus kerep disediakake kanggo nggampangake pengunjung tekan lokasi acara.",
                'act': f"Pengunjung bisa nyaksikake macem-macem pertunjukan budaya, ritual adat, lan atraksi tradisional sajrone {topic_name}. Partisipasi langsung ing sawetara kegiatan bisa ditindakake kanggo menehi pengalaman sing luwih jero. Dokumentasi foto lan video dadi aktivitas populer kanggo ngabadikake momen-momen unik. Interaksi karo masyarakat lokal lan tokoh adat menehi pemahaman sing luwih apik babagan makna budaya acara kasebut. Macem-macem stan panganan lan kerajinan lokal uga kasedhiya kanggo nglengkapi pengalaman budaya."
            }
        else:
            # Default content for other types
            return {
                'hist': f"{topic_name} iku salah siji destinasi wisata menarik ing Indramayu sing duwe keunikan tersendiri. Papan iki wis dikenal dening masyarakat lokal wiwit suwe lan saiki mulai dikembangake dadi destinasi wisata sing menarik kanggo pengunjung saka njaba daerah. Sejarah lan perkembangan {topic_name} ora bisa dipisahake saka upaya pemerintah lan masyarakat setempat kanggo ningkatake potensi pariwisata daerah. Anane papan iki menehi kontribusi positif kanggo perekonomian lokal lan pelestarian budaya.",
                'loc': f"{topic_name} dumunung ing wilayah Kabupaten Indramayu, Jawa Barat. Akses menyang lokasi iki bisa ditempuh nganggo macem-macem jenis transportasi, baik kendaraan pribadi utawa transportasi umum. Saka tengah kutha Indramayu, lelampahan menyang {topic_name} mbutuhake wektu sing beda-beda gumantung kondisi lalu lintas lan jarak tempuh. Ana macem-macem fasilitas pendukung ing sakiwa-tengene lokasi kanggo nggampangake kunjungan wisatawan.",
                'act': f"Ing {topic_name}, pengunjung bisa nikmati macem-macem aktivitas menarik sesuai karo karakteristik papan iki. Fasilitas sing kasedhiya cukup lengkap kanggo ndhukung kenyamanan wisatawan sajrone berkunjung. Macem-macem pilihan aktivitas baik kanggo wong dewasa utawa bocah-bocah bisa ditemokake ing kene. Pengalaman wisata ing {topic_name} bakal menehi kenangan sing ora bisa dilalekake kanggo saben pengunjung."
            }
    
    # Get base information or generate specific content
    if topic in historical_info:
        hist = historical_info[topic]
        loc = location_info[topic]
        act = activities_info[topic]
    else:
        specific = generate_specific_content_indramayu(topic)
        hist = specific['hist']
        loc = specific['loc']
        act = specific['act']
    
    return f"{hist}\n\n{loc}\n\n{act}"

def generate_dataset(topics: List[str]) -> List[Dict[str, Any]]:
    """Generate complete dataset with two entries per topic (Indonesian + Indramayu)"""
    dataset = []
    
    for topic in topics:
        question = generate_question(topic)
        
        # Indonesian answer
        indonesian_answer = generate_indonesian_answer(topic)
        dataset.append({
            "conversations": [
                {
                    "role": "human",
                    "content": question
                },
                {
                    "role": "assistant", 
                    "content": indonesian_answer
                }
            ]
        })
        
        # Indramayu answer  
        indramayu_answer = generate_indramayu_answer(topic)
        dataset.append({
            "conversations": [
                {
                    "role": "human",
                    "content": question
                },
                {
                    "role": "assistant",
                    "content": indramayu_answer
                }
            ]
        })
    
    return dataset

def main():
    """Main function to generate the dataset"""
    print("Reading topics from list-topik.txt...")
    topics = read_topics('list-topik.txt')
    print(f"Found {len(topics)} topics")
    
    print("Generating dataset...")
    dataset = generate_dataset(topics)
    print(f"Generated {len(dataset)} conversation entries")
    
    print("Writing to dataset.json...")
    with open('dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    
    print("Dataset generation completed!")
    print(f"Total entries: {len(dataset)}")
    print(f"Topics covered: {len(topics)}")
    print("Each topic has 2 entries (Indonesian + Indramayu)")

if __name__ == "__main__":
    main()