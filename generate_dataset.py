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
    
    # Get base information or create generic one
    hist = historical_info.get(topic, f"{topic} adalah salah satu destinasi wisata menarik di Indramayu yang memiliki keunikan tersendiri. Tempat ini telah dikenal oleh masyarakat lokal sejak lama dan kini mulai dikembangkan sebagai destinasi wisata yang menarik bagi pengunjung dari luar daerah. Sejarah dan perkembangan {topic} tidak lepas dari upaya pemerintah dan masyarakat setempat untuk meningkatkan potensi pariwisata daerah.")
    
    loc = location_info.get(topic, f"{topic} berlokasi di wilayah Kabupaten Indramayu, Jawa Barat. Akses menuju lokasi ini dapat ditempuh dengan berbagai jenis transportasi, baik kendaraan pribadi maupun transportasi umum. Dari pusat kota Indramayu, perjalanan menuju {topic} memerlukan waktu yang bervariasi tergantung kondisi lalu lintas dan jarak tempuh. Tersedia berbagai fasilitas pendukung di sekitar lokasi untuk memudahkan kunjungan wisatawan.")
    
    act = activities_info.get(topic, f"Di {topic}, pengunjung dapat menikmati berbagai aktivitas menarik sesuai dengan karakteristik tempat ini. Fasilitas yang tersedia cukup lengkap untuk mendukung kenyamanan wisatawan selama berkunjung. Berbagai pilihan aktivitas baik untuk dewasa maupun anak-anak dapat ditemukan di sini. Pengalaman berwisata di {topic} akan memberikan kenangan yang tak terlupakan bagi setiap pengunjung.")
    
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
    
    # Get base information or create generic one
    hist = historical_info.get(topic, f"{topic} iku salah siji destinasi wisata menarik ing Indramayu sing duwe keunikan tersendiri. Papan iki wis dikenal dening masyarakat lokal wiwit suwe lan saiki mulai dikembangake dadi destinasi wisata sing menarik kanggo pengunjung saka njaba daerah. Sejarah lan perkembangan {topic} ora bisa dipisahake saka upaya pemerintah lan masyarakat setempat kanggo ningkatake potensi pariwisata daerah.")
    
    loc = location_info.get(topic, f"{topic} dumunung ing wilayah Kabupaten Indramayu, Jawa Barat. Akses menyang lokasi iki bisa ditempuh nganggo macem-macem jenis transportasi, baik kendaraan pribadi utawa transportasi umum. Saka tengah kutha Indramayu, lelampahan menyang {topic} mbutuhake wektu sing beda-beda gumantung kondisi lalu lintas lan jarak tempuh. Ana macem-macem fasilitas pendukung ing sakiwa-tengene lokasi kanggo nggampangake kunjungan wisatawan.")
    
    act = activities_info.get(topic, f"Ing {topic}, pengunjung bisa nikmati macem-macem aktivitas menarik sesuai karo karakteristik papan iki. Fasilitas sing kasedhiya cukup lengkap kanggo ndhukung kenyamanan wisatawan sajrone berkunjung. Macem-macem pilihan aktivitas baik kanggo wong dewasa utawa bocah-bocah bisa ditemokake ing kene. Pengalaman wisata ing {topic} bakal menehi kenangan sing ora bisa dilalekake kanggo saben pengunjung.")
    
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