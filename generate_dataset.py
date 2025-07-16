#!/usr/bin/env python3
"""
Generate high-quality JSON training data for conversational AI model.
Based on tourism topics in Indramayu with detailed answers in both 
Bahasa Indonesia and Bahasa Indramayu.
"""

import json
import random
from typing import List, Dict, Any

def load_topics(file_path: str) -> List[str]:
    """Load tourism topics from file."""
    topics = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('Berikut') and line != '':
                topics.append(line)
    return topics

def generate_question_variations(topic: str) -> List[str]:
    """Generate varied questions for a topic."""
    question_templates = [
        f"Bisakah Anda menjelaskan tentang {topic}?",
        f"Apa saja yang menarik di {topic}?",
        f"Bagaimana sejarah {topic}?",
        f"Apa aktivitas yang bisa dilakukan di {topic}?",
        f"Ceritakan tentang {topic}.",
        f"Di mana lokasi {topic}?",
        f"Apa yang unik dari {topic}?",
        f"Bagaimana cara menuju {topic}?",
        f"Kapan waktu terbaik mengunjungi {topic}?",
        f"Apa saja fasilitas di {topic}?",
        f"Berapa biaya masuk ke {topic}?",
        f"Apakah {topic} cocok untuk wisata keluarga?",
        f"Apa tips berkunjung ke {topic}?",
        f"Makanan khas apa yang ada di {topic}?",
        f"Bagaimana kondisi {topic} saat ini?",
        f"Apa saja yang ada di {topic}?",
        f"Ceritakna tentang {topic}.",  # Indramayu style
        f"Apa yang menarik dari {topic}?",
        f"Bagaimana sejarah {topic}?",
        f"Di mana lokasi {topic} di endi?",  # Indramayu style
        f"Pira regane mlebu {topic}?",  # Indramayu style
        f"Bagaimana cara menuju {topic} adalah piye?",  # Indramayu style
        f"Apa saja aktivitas yang bisa dilakukan di {topic}?",
        f"Apakah ada festival atau acara khusus di {topic}?",
        f"Apa saja fasilitas di {topic} ada apa saja?",  # Indramayu style
        f"Makanan khas apa yang ada di {topic} apa saja?",  # Indramayu style
        f"Apa tips berkunjung ke {topic} apa saja?",  # Indramayu style
        f"Bagaimana kondisi {topic} sakiyen adalah piye?",  # Indramayu style
        f"Bagaimana sejarah {topic} adalah piye?",  # Indramayu style
        f"Apakah ada acara khusus di {topic}?",
        f"Apa saja aktivitas yang bisa dilakukan di {topic}?",
    ]
    
    return question_templates

def generate_indonesian_answer(topic: str, question_type: str = "general") -> str:
    """Generate detailed Indonesian answer about a tourism topic."""
    
    # Enhanced base information for different types of places
    tourism_data = {
        "Pulau Biawak": {
            "history": "Pulau Biawak merupakan pulau kecil yang terletak di Laut Jawa, sekitar 40 kilometer dari pantai utara Indramayu. Pulau ini mendapat namanya dari populasi biawak monitor (Varanus salvator) yang menghuni pulau tersebut secara alami sejak ribuan tahun yang lalu. Dalam sejarah maritime Indramayu, pulau ini telah menjadi landmark penting bagi para nelayan yang melaut ke perairan lepas. Catatan sejarah menunjukkan bahwa pulau ini pernah digunakan sebagai pos pengamatan pada masa kolonial Belanda untuk mengawasi jalur pelayaran di Laut Jawa.",
            "location": "Pulau Biawak dapat diakses melalui Pelabuhan Karangsong dengan menggunakan perahu nelayan tradisional atau speedboat modern. Perjalanan laut memakan waktu sekitar 3-4 jam tergantung kondisi cuaca dan jenis kapal yang digunakan. Pelabuhan Karangsong sendiri berjarak sekitar 25 kilometer dari pusat kota Indramayu dan dapat ditempuh dengan kendaraan bermotor melalui jalur pantai utara yang menawarkan pemandangan sawah dan tambak ikan yang indah sepanjang perjalanan.",
            "attractions": "Daya tarik utama Pulau Biawak adalah populasi biawak liar yang dapat diamati dalam habitat aslinya, dengan ukuran yang dapat mencapai 2 meter panjangnya. Pulau ini juga menawarkan pantai berpasir putih yang masih alami, air laut yang jernih dengan visibilitas mencapai 15 meter yang sangat cocok untuk snorkeling dan diving. Terumbu karang di sekitar pulau masih dalam kondisi baik dengan berbagai jenis ikan tropis yang berwarna-warni. Pengunjung juga dapat melihat berbagai jenis burung laut seperti camar, pecuk, dan bangau yang bersarang di tebing-tebing pulau.",
            "culture": "Masyarakat nelayan setempat menganggap Pulau Biawak sebagai tempat yang sakral dan memiliki nilai spiritual tinggi. Terdapat kepercayaan lokal bahwa biawak-biawak di pulau ini adalah penjaga spiritual yang melindungi laut dari marabahaya. Tradisi turun temurun mengajarkan pantangan untuk tidak mengganggu atau memburu biawak, serta kewajiban menjaga kebersihan pulau. Para nelayan sering melakukan ritual sederhana sebelum mendarat di pulau sebagai bentuk penghormatan kepada penguasa spiritual pulau.",
            "events": "Meskipun tidak ada festival besar yang diselenggarakan di pulau ini karena kondisi geografisnya, namun periode terbaik untuk berkunjung adalah saat musim kemarau (April-Oktober) ketika cuaca lebih bersahabat untuk perjalanan laut. Beberapa komunitas pecinta alam dan fotografer underwater sesekali mengadakan ekspedisi penelitian marine life dan konservasi terumbu karang. Pada bulan purnama, beberapa wisatawan khusus datang untuk menyaksikan fenomena biawak yang lebih aktif pada malam hari."
        },
        "Pantai Karangsong": {
            "history": "Pantai Karangsong memiliki sejarah panjang sebagai pusat aktivitas maritim di Indramayu yang sudah berlangsung sejak abad ke-15. Sejak zaman Kerajaan Cirebon dan kemudian pada masa kolonial Belanda, kawasan ini telah menjadi pelabuhan penting untuk ekspor hasil pertanian seperti beras dan perikanan tangkap. Nama 'Karangsong' berasal dari bahasa Sunda kuno yang berarti 'tempat berlabuh yang aman', menggambarkan fungsi historisnya sebagai pelabuhan alami yang terlindung dari gelombang besar Laut Jawa.",
            "location": "Pantai Karangsong terletak di Desa Karangsong, Kecamatan Indramayu, sekitar 25 kilometer sebelah utara kota Indramayu melalui jalur Pantura. Akses menuju pantai ini sangat mudah dengan kendaraan pribadi maupun transportasi umum seperti bus atau angkutan pedesaan. Jalan menuju lokasi sudah beraspal mulus dan dilengkapi dengan rambu-rambu petunjuk arah yang jelas. Sepanjang perjalanan, pengunjung akan disuguhi pemandangan persawahan hijau dan tambak-tambak ikan bandeng yang menjadi ciri khas wilayah pesisir Indramayu.",
            "attractions": "Pantai ini menawarkan pemandangan laut yang menawan dengan deretan perahu-perahu nelayan tradisional yang berwarna-warni yang disebut 'jukung'. Pengunjung dapat menyaksikan secara langsung aktivitas nelayan mulai dari pemberangkatan di pagi buta hingga pelelangan ikan sore hari di Tempat Pelelangan Ikan (TPI). Kuliner seafood segar seperti kepiting, udang windu, dan berbagai jenis ikan laut tersedia di warung-warung makan di sepanjang pantai. Sunset di pantai Karangsong sangat memukau dengan siluet perahu nelayan yang menciptakan panorama romantis yang sering dijadikan spot fotografi.",
            "culture": "Karangsong merupakan jantung budaya maritim Indramayu dengan tradisi nelayan yang telah berlangsung turun temurun selama ratusan tahun. Masyarakat setempat masih kental mempertahankan tradisi upacara 'tolak bala' atau sedekah laut untuk keselamatan para nelayan yang melaut. Sistem gotong royong dalam komunitas nelayan masih sangat kuat, mulai dari pemeliharaan perahu hingga pembagian hasil tangkapan. Kehidupan sosial ekonomi masyarakat sangat dipengaruhi oleh siklus pasang surut dan musim penangkapan ikan berdasarkan kalender tradisional Jawa.",
            "events": "Setiap tahun biasanya pada bulan Muharram atau awal tahun Hijriah diadakan Festival Sedekah Laut Karangsong yang menampilkan parade perahu hias, pertunjukan kesenian Tarling (gitar dan suling), tari Topeng Indramayu, dan pameran hasil laut. Upacara Nadran atau Sedekah Laut juga rutin diselenggarakan di pantai ini sebagai bentuk syukur atas hasil tangkapan ikan yang melimpah dan permohonan keselamatan nelayan. Festival kuliner seafood juga sering diadakan untuk mempromosikan kekayaan hasil laut Indramayu."
        }
    }
    
    # Get specific data or use general template
    if topic in tourism_data:
        data = tourism_data[topic]
        return f"{data['history']}\\n\\n{data['location']}\\n\\n{data['attractions']} {data['culture']} {data['events']}"
    
    # Enhanced general templates for locations not specifically defined
    base_answers = [
        f"{topic} merupakan destinasi wisata yang sangat menarik di Indramayu dengan sejarah yang kaya dan keunikan tersendiri yang memukau setiap pengunjung. Tempat ini telah menjadi bagian penting dari pengembangan pariwisata daerah dan menawarkan pengalaman yang tak terlupakan bagi setiap wisatawan yang berkunjung. Latar belakang historisnya mencerminkan perpaduan harmonis budaya Jawa, Sunda, dan pengaruh Islam yang khas di wilayah pesisir utara Jawa, menciptakan identitas budaya yang unik dan otentik.\\n\\nLokasi {topic} sangat strategis dan mudah diakses dari berbagai arah menggunakan kendaraan pribadi maupun transportasi umum yang tersedia secara reguler. Infrastruktur jalan yang memadai dan sistem petunjuk arah yang jelas membuat perjalanan menuju lokasi menjadi nyaman, aman, dan menyenangkan untuk semua kalangan pengunjung. Fasilitas pendukung seperti area parkir yang luas, toilet umum yang bersih, dan warung makan telah tersedia dengan baik untuk menunjang kenyamanan wisatawan.\\n\\n{topic} menawarkan beragam aktivitas menarik mulai dari wisata alam yang memanjakan mata, wisata budaya yang edukatif, hingga kuliner khas daerah yang menggugah selera. Keindahan alamnya yang masih terjaga dengan baik, keramahan masyarakat setempat yang legendaris, dan kearifan lokal yang masih dilestarikan dengan penuh dedikasi menjadi daya tarik utama yang tidak ada tandingannya. Selain itu, berbagai festival dan acara budaya yang diselenggarakan secara rutin sepanjang tahun menambah kekayaan pengalaman wisata di tempat ini, menjadikan setiap kunjungan sebagai momen berkesan dan edukatif.",
        
        f"Sejarah panjang {topic} tidak terlepas dari perkembangan peradaban di wilayah Indramayu yang telah berlangsung selama berabad-abad dengan dinamika yang sangat menarik. Tempat ini menyimpan berbagai cerita dan legenda yang turun temurun diwariskan oleh para sesepuh dan masyarakat setempat dengan penuh kebanggaan. Nilai-nilai historis dan budaya yang terkandung di dalamnya menjadikan lokasi ini tidak hanya sebagai objek wisata biasa, tetapi juga sebagai pusat pembelajaran tentang kearifan lokal dan warisan leluhur yang berharga. Setiap sudut tempat ini memiliki kisah unik yang menggambarkan perjalanan peradaban Indramayu.\\n\\nAkses menuju {topic} telah diperbaiki secara signifikan seiring dengan komitmen pemerintah daerah dalam pengembangan infrastruktur pariwisata di Kabupaten Indramayu. Berbagai moda transportasi tersedia untuk memudahkan perjalanan wisatawan, mulai dari angkutan umum yang terjangkau hingga layanan wisata yang lebih eksklusif dan berkualitas tinggi. Kondisi jalan yang terus diperbaiki dan ketersediaan fasilitas pendukung yang memadai membuat kunjungan menjadi lebih praktis, efisien, dan nyaman untuk semua kategori pengunjung.\\n\\nDaya tarik utama {topic} terletak pada perpaduan yang sempurna antara keindahan alam yang masih asri dan kekayaan budaya yang dimilikinya secara turun temurun. Pengunjung dapat menikmati berbagai aktivitas rekreasi yang menyegarkan jiwa, belajar tentang tradisi lokal yang unik dan autentik, serta merasakan kehangatan hospitalitas masyarakat Indramayu yang terkenal ramah dan grapyak. Program-program wisata edukasi, workshop budaya, dan event-event tradisional yang diselenggarakan secara berkala turut memperkaya pengalaman wisata di lokasi ini.",
        
        f"Kemegahan {topic} telah dikenal sejak zaman dahulu sebagai salah satu ikon wisata Indramayu yang memiliki nilai sejarah tinggi dan makna spiritual yang mendalam bagi masyarakat setempat. Perjalanan panjang dalam pembentukan identitas tempat ini mencerminkan dinamika kehidupan masyarakat pesisir dengan segala tradisi, adat istiadat, dan kearifan lokal yang telah diwariskan turun temurun. Setiap sudut lokasi menyimpan memori kolektif masyarakat tentang perjalanan waktu, transformasi budaya, dan adaptasi terhadap perubahan zaman yang terjadi.\\n\\nPosisi strategis {topic} memberikan kemudahan akses bagi pengunjung dari berbagai wilayah, tidak hanya dari Indramayu sendiri tetapi juga dari kabupaten-kabupaten tetangga dan kota-kota besar di Jawa Barat. Infrastruktur transportasi yang terus dikembangkan menjadikan perjalanan menuju lokasi semakin nyaman, aman, dan terjangkau untuk semua kalangan wisatawan. Ketersediaan berbagai pilihan transportasi memungkinkan wisatawan untuk memilih cara perjalanan yang paling sesuai dengan preferensi, budget, dan kebutuhan individual mereka.\\n\\nPesona {topic} terletak pada kekayaan atraksi wisata yang ditawarkannya, mulai dari keindahan alam yang memukau mata hingga warisan budaya yang otentik dan terjaga dengan baik. Interaksi langsung dengan masyarakat lokal memberikan pengalaman cultural immersion yang mendalam dan berkesan. Berbagai festival, perayaan tradisional, dan acara budaya yang rutin diselenggarakan menjadi momen istimewa untuk merasakan semangat kebersamaan, gotong royong, dan kearifan lokal yang masih terjaga dengan baik di tengah modernisasi yang terus berkembang."
    ]
    
    return random.choice(base_answers)

def generate_indramayu_answer(topic: str, question_type: str = "general") -> str:
    """Generate detailed Indramayu language answer about a tourism topic."""
    
    # Enhanced Indramayu language with specific tourism data
    tourism_data_indramayu = {
        "Pulau Biawak": {
            "history": "Pulau Biawak iku pulau cilik sing ana ning Laut Jawa, kira-kira 40 kilometer saka pesisir lor Indramayu. Asal jenenge Pulau Biawak iku amarga ana akeh biawak gedhe-gedhe (Varanus salvator) sing urip ning kono wiwit jaman biyen. Ning sejarah pelayaran Indramayu, pulau iki wis dadi tandha penting kanggo para nelayan sing mlaku menyang segara jero. Cathetan sejarah nuduhake yen pulau iki tau digunakake minangka pos pengawasan nalika jaman kolonial Walanda kanggo ngawasi jalur kapal ning Laut Jawa.",
            "location": "Kanggo tekan Pulau Biawak, kudu lunga saka Pelabuhan Karangsong nganggo prahu nelayan tradisional utawa speedboat modern. Perjalanan ning segara butuh wektu kira-kira 3-4 jam gumantung kondisi cuaca lan jenis prahu sing digunakake. Pelabuhan Karangsong dhewe jarakne kira-kira 25 kilometer saka kutha Indramayu lan bisa ditempuh nganggo motor lewat jalur pesisir lor sing apik banget pemandangane sawah lan tambak iwak.",
            "attractions": "Daya tarik utama Pulau Biawak yaiku biawak-biawak liar sing bisa dideleng ning habitat asliye, ukurane bisa nganti 2 meter dawane. Pulau iki uga duwe pantai pasir putih sing isih alami, banyu segara sing bening kanthi visibilitas nganti 15 meter sing apik banget kanggo snorkeling lan diving. Terumbu karang ning sakubenge pulau isih apik banget karo macem-macem iwak tropis sing warna-warni. Pengunjung uga bisa ndeleng macem-macem manuk segara kaya camar, pecuk, lan bangau sing nggawe susuh ning tebing-tebing pulau.",
            "culture": "Masyarakat nelayan setempat nganggep Pulau Biawak minangka papan sing kramat lan nduweni nilai spiritual dhuwur. Ana kapercayan lokal yen biawak-biawak ning pulau iki yaiku penjaga spiritual sing ngreksa segara saka bebaya. Tradisi turun temurun mulang pantangan ora kena ngganggu utawa mburu biawak, uga kudu njaga kebersihan pulau. Para nelayan kerep nindakake ritual sederhana sadurunge mlebu pulau minangka wujud pakurmatan marang panguasa spiritual pulau.",
            "events": "Senadyan ora ana festival gedhe sing diselenggarake ning pulau iki amarga kondisi geografise, nanging wektu paling apik kanggo berkunjung yaiku nalika musim kemarau (April-Oktober) nalika cuaca luwih bersahabat kanggo perjalanan segara. Sawetara komunitas pecinta alam lan fotografer underwater kadang-kadang nganakake ekspedisi riset marine life lan konservasi terumbu karang. Nalika purnama, sawetara wisatawan khusus teka kanggo ndeleng fenomena biawak sing luwih aktif ning wayah bengi."
        },
        "Pantai Karangsong": {
            "history": "Pantai Karangsong nduweni sejarah dawa minangka pusat aktivitas maritim ning Indramayu sing wis lumaku wiwit abad kaping 15. Wiwit jaman Kerajaan Cirebon banjur nalika masa kolonial Walanda, wilayah iki wis dadi pelabuhan penting kanggo ekspor asil tetanen kaya beras lan iwak tangkapan. Jeneng 'Karangsong' asale saka basa Sunda kuna sing tegese 'papan berlabuh sing aman', nggambarake fungsine minangka pelabuhan alami sing terlindung saka ombak gedhe Laut Jawa.",
            "location": "Pantai Karangsong ana ning Desa Karangsong, Kecamatan Indramayu, kira-kira 25 kilometer sisih lor kutha Indramayu lewat jalur Pantura. Aksese menyang pantai iki gampang banget nganggo kendaraan pribadi utawa transportasi umum kaya bis utawa angkutan pedesaan. Dalane menyang lokasi wis diaspal alus lan dilengkapi rambu-rambu petunjuk arah sing jelas. Sepanjang perjalanan, pengunjung bakal disuguhi pemandangan sawah ijo lan tambak-tambak iwak bandeng sing dadi ciri khas wilayah pesisir Indramayu.",
            "attractions": "Pantai iki nawakake pemandangan segara sing asri karo deretan prahu-prahu nelayan tradisional sing warna-warni sing diarani 'jukung'. Pengunjung bisa ndeleng langsung aktivitas nelayan wiwit budhal ning esuk-esuk nganti lelangan iwak sore ning Tempat Pelelangan Ikan (TPI). Kuliner seafood seger kaya kepiting, udang windu, lan macem-macem iwak segara kasedhiya ning warung-warung makan sepanjang pantai. Sunset ning pantai Karangsong apik banget karo siluet prahu nelayan sing nggawe panorama romantis sing kerep dadi spot fotografi.",
            "culture": "Karangsong minangka jantunge budaya maritim Indramayu karo tradisi nelayan sing wis lumaku turun temurun sajrone atusan taun. Masyarakat setempat isih kental njaga tradisi upacara 'tolak bala' utawa sedekah segara kanggo kaslametan para nelayan sing mlaku. Sistem gotong royong ning komunitas nelayan isih kuwat banget, wiwit saka ngopeni prahu nganti mbagi asil tangkapan. Urip sosial ekonomi masyarakat banget dipengaruhi dening siklus pasang surut lan musim panangkapan iwak miturut kalender tradisional Jawa.",
            "events": "Saben taun biasane ning wulan Muharram utawa awal taun Hijriah dianakake Festival Sedekah Segara Karangsong sing nampilake parade prahu hias, pertunjukan kesenian Tarling (gitar lan suling), tari Topeng Indramayu, lan pameran asil segara. Upacara Nadran utawa Sedekah Segara uga rutin diselenggarake ning pantai iki minangka wujud syukur marang asil tangkapan iwak sing akeh lan panjaluk kaslametan nelayan. Festival kuliner seafood uga kerep dianakake kanggo promosi kekayaan asil segara Indramayu."
        }
    }
    
    # Get specific data or use general template
    if topic in tourism_data_indramayu:
        data = tourism_data_indramayu[topic]
        return f"{data['history']}\\n\\n{data['location']}\\n\\n{data['attractions']} {data['culture']} {data['events']}"
    
    # Enhanced general templates for locations not specifically defined
    base_answers = [
        f"{topic} iku panggonan wisata sing menarik banget ning Indramayu kanthi sejarah sing sugih lan keunikan dhewe-dhewe. Papan iki wis dadi bagian penting kanggo pangembangan pariwisata daerah lan nawakake pengalaman sing ora bakal lali kanggo saben pengunjung. Latar mburi sejarahe nggambarake campuran budaya Jawa, Sunda, lan pengaruh Islam sing khas ning wilayah pesisir lor Jawa. Wiwit jaman biyen, papan iki wis dikenal minangka salah siji destinasi unggulan sing nduweni daya tarik tersendiri.\\n\\nLokasi {topic} posisine strategis banget lan gampang diakses saka macem-macem arah nganggo kendaraan pribadi utawa transportasi umum. Fasilitas dalan sing memadai lan petunjuk arah sing jelas gawe perjalanan menyang lokasi dadi nyaman lan seneng-seneng. Infrastruktur pendukung kaya area parkir, toilet umum, lan warung makan wis tersedia kanthi apik kanggo kenyamanan pengunjung.\\n\\n{topic} nawakake macem-macem aktivitas menarik wiwit saka wisata alam, budaya, nganti kuliner khas daerah Indramayu. Ayu alame sing isih dijaga kanthi apik, keramahan masyarakat setempat sing grapyak, lan kearifan lokal sing isih dilestarikan dadi daya tarik utama sing ora ana tandhingane. Kajaba iku, macem-macem festival lan acara budaya sing diselenggarake kanthi rutin nambah kekayaan pengalaman wisata ning panggonan iki, ndadekake saben kunjungan dadi berkesan lan edukatif.",
        
        f"Sejarah {topic} ora bisa dipisahke saka perkembangan peradaban ning wilayah Indramayu sing wis lumaku sajrone atusan taun. Panggonan iki nyimpen macem-macem crita lan legenda sing turun temurun diwarisake dening para sesepuh lan masyarakat setempat. Nilai-nilai sejarah lan budaya sing ana ing jerone ndadekake lokasi iki ora mung dadi obyek wisata biasa, nanging uga dadi pusat sinau babagan kearifan lokal lan warisan leluhur. Saben pojok papan iki nduweni crita unik sing nggambarake perjalanan peradaban Indramayu.\\n\\nAkses menyang {topic} wis diperbaiki seiring karo pangembangan infrastruktur pariwisata ning kabupaten Indramayu. Macem-macem moda transportasi kasedhiya kanggo gampangake perjalanan wisatawan, wiwit saka angkutan umum sing murah meriah nganti layanan wisata sing luwih eksklusif lan nyaman. Kondisi dalan sing wis diaspal apik lan kasedhiyane fasilitas pendukung gawe kunjungan dadi luwih praktis, aman, lan efisien kanggo kabeh kalangan pengunjung.\\n\\nDaya tarik utama {topic} ana ning campuran harmonis antara keindahan alam sing masih asri lan kekayaan budaya sing diduweni. Pengunjung bisa nikmati macem-macem aktivitas rekreasi sing nyenenangke, sinau babagan tradisi lokal sing unik, lan ngrasakake anggete hospitalitas masyarakat Indramayu sing grapyak. Program-program wisata edukasi, workshop budaya, lan event-event tradisional sing diselenggarake kanthi berkala uga memperkaya pengalaman wisata ning lokasi iki.",
        
        f"Kemegahan {topic} wis dikenal wiwit jaman biyen minangka salah siji ikon wisata Indramayu sing nduweni nilai sejarah dhuwur lan makna spiritual sing jero. Perjalanan dawa ing pembentukan identitas panggonan iki nggambarake dinamika kehidupan masyarakat pesisir karo kabeh tradisi, adat istiadat, lan kearifan lokal sing wis turun temurun. Saben pojok lokasi nyimpen memori kolektif masyarakat babagan perjalanan wektu, transformasi budaya, lan adaptasi terhadap perubahan jaman sing kedadeyan.\\n\\nPosisi strategis {topic} menehi kemudahan akses kanggo pengunjung saka macem-macem wilayah, ora mung saka Indramayu dhewe nanging uga saka kabupaten-kabupaten tetangga. Infrastruktur transportasi sing terus dikembangake ndadekake perjalanan menyang lokasi tambah nyaman, aman, lan terjangkau kanggo kabeh kalangan wisatawan. Kasedhiyane macem-macem pilihan transportasi ngidini wisatawan kanggo milih cara perjalanan sing paling cocok karo preferensi, budget, lan kebutuhan individual.\\n\\nPesona {topic} ana ning kekayaan atraksi wisata sing ditawakake, wiwit saka keindahan alam sing memukau mata nganti warisan budaya sing otentik lan terjaga apik. Interaksi langsung karo masyarakat lokal menehi pengalaman cultural immersion sing jero lan berkesan. Macem-macem festival, perayaan tradisional, lan acara budaya sing rutin diselenggarake dadi momen istimewa kanggo ngrasakake semangat kebersamaan, gotong royong, lan kearifan lokal sing isih dijaga kanthi apik dening masyarakat Indramayu."
    ]
    
    return random.choice(base_answers)

def generate_conversation_pair(topic: str, question: str) -> List[Dict[str, Any]]:
    """Generate a pair of conversations for the same question in both languages."""
    
    # Indonesian conversation
    indonesian_conversation = {
        "conversations": [
            {
                "role": "human",
                "content": question
            },
            {
                "role": "assistant", 
                "content": generate_indonesian_answer(topic)
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
                "content": generate_indramayu_answer(topic)
            }
        ]
    }
    
    return [indonesian_conversation, indramayu_conversation]

def generate_dataset(topics: List[str], target_conversations: int = 10000) -> List[Dict[str, Any]]:
    """Generate the complete dataset with the specified number of conversations."""
    
    conversations = []
    conversations_per_topic = target_conversations // len(topics)
    
    for topic in topics:
        questions = generate_question_variations(topic)
        
        # Generate conversations for this topic
        topic_conversations = 0
        question_index = 0
        
        while topic_conversations < conversations_per_topic:
            # Use questions cyclically
            question = questions[question_index % len(questions)]
            
            # Generate conversation pair (Indonesian + Indramayu)
            pair = generate_conversation_pair(topic, question)
            conversations.extend(pair)
            
            topic_conversations += 2  # We added 2 conversations
            question_index += 1
    
    # Shuffle to mix languages and topics
    random.shuffle(conversations)
    
    # Trim to exact target if needed
    return conversations[:target_conversations]

def main():
    """Main function to generate the dataset."""
    print("Loading topics from list-topik.txt...")
    topics = load_topics('list-topik.txt')
    print(f"Found {len(topics)} topics")
    
    print("Generating dataset...")
    dataset = generate_dataset(topics, 10000)
    
    print(f"Generated {len(dataset)} conversations")
    print(f"Saving to dataset.json...")
    
    with open('dataset.json', 'w', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
    
    print("Dataset generation completed!")
    
    # Print some statistics
    indonesian_count = sum(1 for conv in dataset if any('adalah' in msg['content'] or 'merupakan' in msg['content'] for msg in conv['conversations'] if msg['role'] == 'assistant'))
    indramayu_count = sum(1 for conv in dataset if any('sing' in msg['content'] or 'ning' in msg['content'] for msg in conv['conversations'] if msg['role'] == 'assistant'))
    
    print(f"Estimated Indonesian conversations: {indonesian_count}")
    print(f"Estimated Indramayu conversations: {indramayu_count}")

if __name__ == "__main__":
    main()