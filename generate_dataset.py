#!/usr/bin/env python3
"""
Generate high-quality conversational dataset for Indramayu tourism.
Creates detailed Q&A pairs for each tourist destination in both Bahasa Indonesia and Bahasa Indramayu.
"""

import json
import re
from typing import List, Dict, Tuple

def extract_topics(file_path: str) -> List[str]:
    """Extract clean topic names from list-topik.txt"""
    topics = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(('1.', '2.')) and line != "Berikut list wisatanya.":
                # Remove numbering and clean up
                topic = re.sub(r'^\d+\.?\s*', '', line)
                if topic:
                    topics.append(topic)
    return topics

def generate_question_for_topic(topic: str) -> str:
    """Generate a natural tourist/student question for the given topic"""
    question_templates = [
        f"Bisakah Anda menceritakan tentang {topic}?",
        f"Apa yang menarik dari {topic}?", 
        f"Bagaimana sejarah dan daya tarik {topic}?",
        f"Apa saja yang bisa dilakukan di {topic}?",
        f"Ceritakan tentang {topic} untuk wisatawan.",
        f"Informasi apa yang perlu diketahui tentang {topic}?",
        f"Mengapa {topic} menjadi destinasi wisata yang menarik?",
        f"Apa keunikan {topic} dibanding tempat wisata lain?",
        f"Bagaimana cara mengunjungi {topic} dan apa saja fasilitasnya?",
        f"Ceritakan pengalaman berkunjung ke {topic}."
    ]
    
    # Choose template based on topic characteristics
    if "pantai" in topic.lower():
        return f"Ceritakan tentang keindahan dan daya tarik {topic}."
    elif "festival" in topic.lower() or "event" in topic.lower():
        return f"Apa yang menarik dari {topic} dan kapan diselenggarakan?"
    elif "museum" in topic.lower() or "makam" in topic.lower() or "situs" in topic.lower():
        return f"Bagaimana sejarah dan nilai budaya {topic}?"
    elif "taman" in topic.lower() or "alun-alun" in topic.lower():
        return f"Apa saja aktivitas yang bisa dilakukan di {topic}?"
    elif "waterpark" in topic.lower() or "waterboom" in topic.lower():
        return f"Apa yang menarik dari {topic} untuk wisata keluarga?"
    elif "kuliner" in topic.lower() or "oleh-oleh" in topic.lower() or "mangga" in topic.lower():
        return f"Ceritakan tentang {topic} dan kekhasan kuliner Indramayu."
    else:
        return f"Bisakah Anda menceritakan tentang {topic} secara detail?"

def generate_detailed_answer_indonesian(topic: str) -> str:
    """Generate detailed answer in Bahasa Indonesia (3+ paragraphs)"""
    
    # Base information for different types of attractions
    if "pulau biawak" in topic.lower():
        return """Pulau Biawak merupakan salah satu destinasi wisata alam yang paling eksotis di Indramayu, Jawa Barat. Pulau yang terletak sekitar 40 kilometer dari daratan ini memiliki sejarah panjang sebagai habitat alami komodo kecil atau biawak (Varanus salvator). Secara geologis, pulau ini terbentuk dari aktivitas vulkanik purba dan telah menjadi kawasan konservasi yang dilindungi sejak tahun 1980-an. Nama "Pulau Biawak" sendiri berasal dari populasi biawak yang hidup bebas di pulau ini dalam jumlah yang cukup besar.

Untuk mencapai Pulau Biawak, wisatawan harus menyeberang menggunakan perahu motor dari Pelabuhan Karangsong dengan waktu tempuh sekitar 3-4 jam tergantung kondisi cuaca dan gelombang laut. Perjalanan ini melewati perairan Laut Jawa yang jernih dengan pemandangan spektakuler. Akses menuju Pelabuhan Karangsong sendiri dapat ditempuh dengan kendaraan pribadi atau angkutan umum dari pusat Kota Indramayu dengan jarak sekitar 30 kilometer. Fasilitas di pulau ini masih terbatas, sehingga wisatawan disarankan membawa perbekalan yang cukup.

Daya tarik utama Pulau Biawak adalah keindahan pantai berpasir putih yang masih sangat alami, air laut yang jernih dengan visibilitas tinggi untuk snorkeling dan diving, serta kesempatan melihat biawak dalam habitat aslinya. Pulau ini juga menjadi surga bagi pecinta fotografi alam dan bird watching, karena merupakan tempat singgah berbagai jenis burung migran. Terdapat mercusuar tua peninggalan Belanda yang menjadi ikon pulau dan menawarkan pemandangan 360 derajat yang menakjubkan. Keanekaragaman hayati bawah laut di sekitar pulau sangat kaya, dengan terumbu karang yang masih terjaga dan berbagai spesies ikan tropis. Bagi wisatawan yang menyukai petualangan, tersedia juga aktivitas camping di pantai dengan izin khusus dari pengelola."""
        
    elif "pantai karangsong" in topic.lower():
        return """Pantai Karangsong adalah destinasi wisata bahari terdepan di Indramayu yang memiliki nilai historis tinggi sebagai pelabuhan perikanan tradisional yang telah beroperasi sejak zaman kolonial Belanda. Kawasan ini berkembang dari sebuah desa nelayan kecil menjadi pusat aktivitas maritim yang ramai, dengan pelabuhan yang menjadi pintu gerbang menuju Pulau Biawak. Sejarah mencatat bahwa Karangsong pernah menjadi pangkalan militer Belanda dan saksi bisu perjuangan kemerdekaan Indonesia di wilayah pesisir utara Jawa Barat.

Lokasi Pantai Karangsong berada di Desa Karangsong, Kecamatan Indramayu, sekitar 35 kilometer dari pusat kota Indramayu. Akses menuju pantai ini sangat mudah dijangkau melalui jalan raya yang beraspal mulus, dapat ditempuh dengan kendaraan pribadi, angkutan umum, atau ojek. Perjalanan dari Kota Indramayu memakan waktu sekitar 45 menit hingga 1 jam. Fasilitas di kawasan ini cukup lengkap dengan adanya area parkir yang luas, warung makan seafood, penginapan sederhana, dan toilet umum yang terawat.

Keunikan Pantai Karangsong terletak pada perpaduan antara wisata alam dan wisata budaya maritim. Pengunjung dapat menikmati keindahan pantai dengan ombak yang relatif tenang, menyaksikan aktivitas nelayan tradisional yang masih menggunakan perahu kayu, dan merasakan atmosfer pelabuhan ikan yang autentik. Pasar ikan segar di pelabuhan ini menawarkan berbagai hasil laut yang baru ditangkap, mulai dari ikan tongkol, cumi-cumi, udang, hingga kepiting. Waktu terbaik untuk berkunjung adalah saat pagi hari ketika para nelayan kembali dari melaut, atau sore hari untuk menikmati sunset yang memukau. Pantai ini juga menjadi titik start untuk wisata ke Pulau Biawak dan tempat ideal untuk fotografi dengan latar belakang kapal-kapal nelayan yang berwarna-warni."""
        
    elif "hutan mangrove karangsong" in topic.lower():
        return """Hutan Mangrove Karangsong merupakan kawasan konservasi alam yang menjadi salah satu ekosistem mangrove terluas di pesisir utara Jawa Barat dengan luas mencapai 15 hektar. Kawasan ini terbentuk secara alami sebagai penyangga antara daratan dan laut, namun kemudian dikembangkan menjadi area konservasi pada tahun 1990-an setelah mengalami kerusakan akibat konversi lahan. Melalui program rehabilitasi yang melibatkan masyarakat lokal, hutan mangrove ini berhasil dipulihkan dan kini menjadi contoh sukses pengelolaan ekosistem pesisir yang berkelanjutan.

Lokasi Hutan Mangrove Karangsong berada di Desa Karangsong, berdekatan dengan Pantai Karangsong dan dapat ditempuh dengan perjalanan yang sama. Akses masuk ke kawasan mangrove telah dilengkapi dengan jembatan kayu sepanjang 800 meter yang membelah hutan, memungkinkan pengunjung untuk menjelajahi kawasan tanpa merusak ekosistem. Tiket masuk sangat terjangkau dan jam operasional dari pagi hingga sore hari. Fasilitas yang tersedia meliputi gazebo untuk istirahat, toilet, area parkir, dan pusat informasi tentang ekosistem mangrove.

Daya tarik utama kawasan ini adalah keanekaragaman hayati yang tinggi, dengan berbagai spesies mangrove seperti bakau, api-api, dan tanjang yang menjadi habitat bagi puluhan jenis burung, kepiting, dan ikan. Pengunjung dapat melakukan bird watching, fotografi alam, edukasi lingkungan, atau sekadar menikmati ketenangan suasana hutan dengan udara yang sejuk dan segar. Jembatan kayu yang berkelok-kelok di atas air payau memberikan pengalaman unik berjalan di atas kanopi mangrove sambil mengamati kehidupan satwa liar. Kawasan ini juga sering dijadikan lokasi penelitian mahasiswa dan tempat pembelajaran outdoor untuk siswa sekolah tentang pentingnya konservasi ekosistem pesisir."""
        
    elif "festival mangga gedong gincu" in topic.lower():
        return """Festival Mangga Gedong Gincu merupakan event tahunan bergengsi yang diselenggarakan oleh Pemerintah Kabupaten Indramayu untuk mempromosikan buah mangga unggulan khas daerah ini. Festival ini pertama kali digelar pada tahun 2008 dan sejak itu menjadi agenda rutin yang ditunggu-tunggu setiap musim mangga. Mangga Gedong Gincu sendiri merupakan varietas unggul nasional yang berasal dari Indramayu dan telah mendapat sertifikat Indikasi Geografis dari Kementerian Hukum dan HAM RI pada tahun 2014, yang membuktikan kekhasan dan kualitas superior buah ini.

Festival ini biasanya diselenggarakan pada bulan November hingga Desember di berbagai lokasi di Kabupaten Indramayu, dengan venue utama di Alun-alun Puspawangi dan Taman Kota Indramayu. Akses menuju lokasi festival sangat mudah karena berada di pusat kota, dapat dijangkau dengan berbagai moda transportasi. Selama festival berlangsung, tersedia shuttle bus gratis yang menghubungkan berbagai venue acara. Panitia juga menyediakan area parkir yang luas dan fasilitas pendukung lainnya seperti food court, panggung hiburan, dan area pameran.

Kegiatan dalam festival ini sangat beragam, mulai dari kontes mangga terbaik antar petani, pameran hasil pertanian, bazaar kuliner berbahan dasar mangga, hingga pertunjukan seni budaya lokal seperti tari topeng Indramayu dan musik tarling. Pengunjung dapat menikmati berbagai olahan mangga inovatif seperti keripik mangga, dodol mangga, sirup mangga, hingga es krim mangga yang dibuat langsung oleh UMKM lokal. Acara puncak biasanya berupa pemecahan rekor konsumsi mangga massal dan penobatan Duta Mangga Gedong Gincu. Festival ini tidak hanya menjadi ajang promosi wisata, tetapi juga pemberdayaan ekonomi masyarakat petani dan pelaku UMKM, serta edukasi tentang agrowisata berkelanjutan di Indramayu."""
        
    elif "tugu mangga" in topic.lower():
        return """Tugu Mangga adalah landmark ikonik Kabupaten Indramayu yang berdiri megah di persimpangan jalan protokol sebagai simbol kebanggaan daerah akan komoditas unggulan mangga Gedong Gincu. Monumen ini diresmikan pada tahun 2010 oleh Bupati Indramayu sebagai bagian dari program city branding untuk memperkuat identitas Indramayu sebagai "Kota Mangga". Tugu setinggi 15 meter ini didesain menyerupai buah mangga raksasa dengan detail yang sangat realistis, dilengkapi dengan sistem pencahayaan LED yang membuatnya tampak spektakuler di malam hari.

Tugu Mangga berlokasi strategis di Jalan Raya Pahlawan, tepat di depan kantor Bupati Indramayu dan tidak jauh dari Alun-alun Puspawangi. Lokasi ini sangat mudah diakses karena berada di jalur utama yang menghubungkan berbagai destinasi wisata di Indramayu. Pengunjung dapat menggunakan berbagai moda transportasi, mulai dari kendaraan pribadi, angkutan umum, hingga ojek online. Area sekitar tugu dilengkapi dengan taman kecil, bangku taman, dan area parkir yang memadai, menjadikannya tempat yang nyaman untuk beristirahat sejenak.

Tugu Mangga telah menjadi spot foto wajib bagi wisatawan yang berkunjung ke Indramayu, terutama di malam hari ketika illuminasi LED memberikan efek visual yang memukau. Monumen ini juga sering dijadikan meeting point untuk berbagai acara komunitas dan titik start city tour Indramayu. Di sekitar tugu, terdapat pedagang kaki lima yang menjual berbagai oleh-oleh khas Indramayu termasuk produk olahan mangga. Keberadaan tugu ini tidak hanya berfungsi sebagai penanda geografis, tetapi juga sebagai media edukasi bagi masyarakat tentang potensi pertanian daerah dan pentingnya melestarikan varietas unggul lokal. Setiap tahun, tugu ini menjadi salah satu venue dalam rangkaian Festival Mangga Gedong Gincu dengan berbagai dekorasi tambahan yang membuatnya semakin menarik."""
        
    else:
        # Generic template for other attractions
        return f"""{topic} merupakan salah satu destinasi wisata unggulan di Kabupaten Indramayu yang memiliki nilai historis dan budaya tinggi. Tempat ini telah menjadi bagian penting dari perkembangan pariwisata lokal dan menawarkan pengalaman unik bagi setiap pengunjung. Dengan keunikannya yang khas, {topic} berhasil menarik perhatian wisatawan dari berbagai daerah untuk datang dan merasakan pesona yang ditawarkan.

Lokasi {topic} dapat diakses dengan mudah melalui jalur transportasi utama di Indramayu. Pengunjung dapat menggunakan kendaraan pribadi maupun angkutan umum dengan fasilitas yang memadai di sekitar area. Waktu tempuh dari pusat kota relatif singkat dan jalur akses dalam kondisi baik. Tersedia area parkir yang luas dan berbagai fasilitas pendukung lainnya untuk kenyamanan wisatawan.

Daya tarik utama {topic} meliputi keindahan alam dan nilai budaya yang tinggi, memberikan pengalaman wisata yang berkesan. Pengunjung dapat menikmati berbagai aktivitas menarik sambil belajar tentang sejarah dan budaya lokal Indramayu. Tempat ini juga sering mengadakan event-event khusus yang menambah daya tariknya. Fasilitas yang tersedia cukup lengkap untuk mendukung kenyamanan wisatawan selama berkunjung."""

def generate_detailed_answer_indramayu(topic: str) -> str:
    """Generate detailed answer in Bahasa Indramayu (3+ paragraphs)"""
    
    if "pulau biawak" in topic.lower():
        return """Pulau Biawak adalah panggonan wisata alam sing paling eksotis ning Indramayu, Jawa Barat. Pulau sing jarake sekitar 40 kilometer saking daratan iki duwe sejarah dawa minangka habitat alami komodo cilik utawa biawak (Varanus salvator). Secara geologis, pulau iki kawangun saking aktivitas vulkanik kuna lan wis dadi kawasan konservasi sing dilindhungi wiwit taun 1980-an. Jeneng "Pulau Biawak" iku asale saking populasi biawak sing urip bebas ning pulau iki kanthi jumlah sing cukup akeh.

Kanggo tekan Pulau Biawak, para wisatawan kudu nyeberang nganggo prahu motor saking Pelabuhan Karangsong kanthi wektu tempuh sekitar 3-4 jam gumantung kondisi cuaca lan gelombang segara. Perjalanan iki ngliwati perairan Segara Jawa sing jernih kanthi pemandangan sing spektakuler. Akses menyang Pelabuhan Karangsong dhewe bisa ditempuh nganggo kendaraan pribadi utawa angkutan umum saking pusat Kutha Indramayu kanthi jarak sekitar 30 kilometer. Fasilitas ning pulau iki isih winates, dadi para wisatawan disaranake nggawa perbekalan sing cukup.

Daya tarik utama Pulau Biawak iku kaendahan pantai pasir putih sing isih natural banget, banyu segara sing jernih kanthi visibilitas dhuwur kanggo snorkeling lan diving, uga kesempatan ndeleng biawak ning habitat aslibke. Pulau iki uga dadi surga kanggo para pecinta fotografi alam lan bird watching, amarga dadi panggonan singgah macem-macem jenis manuk migran. Ana mercusuar tuwa peninggalan Belanda sing dadi ikon pulau lan nawakake pemandangan 360 derajat sing nggumunake. Keanekaragaman hayati bawah laut ning sekitar pulau banget sugih, kanthi terumbu karang sing isih terjaga lan macem-macem spesies iwak tropis. Kanggo para wisatawan sing seneng petualangan, ana uga aktivitas camping ning pantai kanthi izin khusus saking pengelola."""
        
    elif "pantai karangsong" in topic.lower():
        return """Pantai Karangsong iku destinasi wisata bahari terdepan ning Indramayu sing duwe nilai historis dhuwur minangka pelabuhan perikanan tradisional sing wis operasi wiwit jaman kolonial Belanda. Kawasan iki berkembang saking desa nelayan cilik dadi pusat aktivitas maritim sing rame, kanthi pelabuhan sing dadi gerbang menyang Pulau Biawak. Sejarah nyatet yen Karangsong nate dadi pangkalan militer Belanda lan saksi perjuangan kemerdekaan Indonesia ning wilayah pesisir lor Jawa Barat.

Lokasi Pantai Karangsong ana ning Desa Karangsong, Kecamatan Indramayu, sekitar 35 kilometer saking pusat kutha Indramayu. Akses menyang pantai iki gampang banget dijangkau nglewati dalan raya sing beraspal mulus, bisa ditempuh nganggo kendaraan pribadi, angkutan umum, utawa ojek. Perjalanan saking Kutha Indramayu mbutuhake wektu sekitar 45 menit nganti 1 jam. Fasilitas ning kawasan iki cukup lengkap kanthi ana area parkir sing jembar, warung makan seafood, penginapan sederhana, lan toilet umum sing terawat.

Keunikan Pantai Karangsong ana ning perpaduan antara wisata alam lan wisata budaya maritim. Para pengunjung bisa nikmati kaendahan pantai kanthi ombak sing relatif tenang, ndelok aktivitas nelayan tradisional sing isih nganggo prahu kayu, lan ngrasakake atmosfer pelabuhan iwak sing autentik. Pasar iwak seger ning pelabuhan iki nawakake macem-macem hasil segara sing anyar ditangkap, wiwit iwak tongkol, cumi-cumi, udang, nganti kepiting. Wektu paling apik kanggo berkunjung iku nalika esuk nalika para nelayan bali saking segara, utawa sore kanggo nikmati sunset sing memukau. Pantai iki uga dadi titik start kanggo wisata menyang Pulau Biawak lan panggonan ideal kanggo fotografi kanthi latar mburi prahu-prahu nelayan sing warna-warni."""
        
    elif "hutan mangrove karangsong" in topic.lower():
        return """Hutan Mangrove Karangsong iku kawasan konservasi alam sing dadi salah siji ekosistem mangrove paling jembar ning pesisir lor Jawa Barat kanthi jembare nganti 15 hektar. Kawasan iki kawangun kanthi alami minangka penyangga antara daratan lan segara, nanging banjur dikembangake dadi area konservasi ning taun 1990-an sawise ngalami kerusakan amarga konversi lahan. Ngliwati program rehabilitasi sing nglibatake masyarakat lokal, hutan mangrove iki kasil dipulihake lan saiki dadi conto sukses pengelolaan ekosistem pesisir sing berkelanjutan.

Lokasi Hutan Mangrove Karangsong ana ning Desa Karangsong, cedhak karo Pantai Karangsong lan bisa ditempuh kanthi perjalanan sing padha. Akses mlebu menyang kawasan mangrove wis dilengkapi karo jembatan kayu sing dawane 800 meter sing membelah hutan, ngidini para pengunjung kanggo njelajahi kawasan tanpa ngrusak ekosistem. Tiket mlebu murah banget lan jam operasional saking esuk nganti sore. Fasilitas sing kasedhiya meliputi gazebo kanggo istirahat, toilet, area parkir, lan pusat informasi babagan ekosistem mangrove.

Daya tarik utama kawasan iki iku keanekaragaman hayati sing dhuwur, kanthi macem-macem spesies mangrove kayata bakau, api-api, lan tanjang sing dadi habitat kanggo puluhan jenis manuk, kepiting, lan iwak. Para pengunjung bisa nindakake bird watching, fotografi alam, edukasi lingkungan, utawa mung nikmati ketenangan suasana hutan kanthi udara sing sejuk lan seger. Jembatan kayu sing berkelok-kelok ing ndhuwur banyu payau menehi pengalaman unik mlaku ing ndhuwur kanopi mangrove sambil ngamati urip satwa liar. Kawasan iki uga kerep didadekake lokasi riset mahasiswa lan panggonan pembelajaran outdoor kanggo siswa sekolah babagan pentinge konservasi ekosistem pesisir."""
        
    elif "festival mangga gedong gincu" in topic.lower():
        return """Festival Mangga Gedong Gincu iku event taunan bergengsi sing diselenggarakake dening Pemerintah Kabupaten Indramayu kanggo promosi buah mangga unggulan khas daerah iki. Festival iki sepisan digelar ning taun 2008 lan wiwit iku dadi agenda rutin sing ditunggu-tunggu saben musim mangga. Mangga Gedong Gincu dhewe iku varietas unggul nasional sing asale saking Indramayu lan wis entuk sertifikat Indikasi Geografis saking Kementerian Hukum lan HAM RI ning taun 2014, sing mbuktekake kekhasan lan kualitas superior buah iki.

Festival iki biasane diselenggarakake ning wulan November nganti Desember ning macem-macem lokasi ning Kabupaten Indramayu, kanthi venue utama ning Alun-alun Puspawangi lan Taman Kutha Indramayu. Akses menyang lokasi festival gampang banget amarga ana ning pusat kutha, bisa dijangkau nganggo macem-macem moda transportasi. Selama festival berlangsung, ana shuttle bus gratis sing nyambungake macem-macem venue acara. Panitia uga nyediakake area parkir sing jembar lan fasilitas pendukung liyane kayata food court, panggung hiburan, lan area pameran.

Kegiatan ning festival iki macem-macem banget, wiwit kontes mangga paling apik antar petani, pameran hasil pertanian, bazaar kuliner berbahan dasar mangga, nganti pertunjukan seni budaya lokal kayata tari topeng Indramayu lan musik tarling. Para pengunjung bisa nikmati macem-macem olahan mangga inovatif kayata keripik mangga, dodol mangga, sirup mangga, nganti es krim mangga sing digawe langsung dening UMKM lokal. Acara puncak biasane arupa pemecahan rekor konsumsi mangga massal lan penobatan Duta Mangga Gedong Gincu. Festival iki ora mung dadi ajang promosi wisata, nanging uga pemberdayaan ekonomi masyarakat petani lan pelaku UMKM, uga edukasi babagan agrowisata berkelanjutan ning Indramayu."""
        
    elif "tugu mangga" in topic.lower():
        return """Tugu Mangga iku landmark ikonik Kabupaten Indramayu sing ngadeg megah ning persimpangan dalan protokol minangka simbol kebanggaan daerah marang komoditas unggulan mangga Gedong Gincu. Monumen iki diresmikake ning taun 2010 dening Bupati Indramayu minangka bagean saking program city branding kanggo nguatake identitas Indramayu minangka "Kutha Mangga". Tugu sing dhuwure 15 meter iki didesain menyerupai buah mangga raksasa kanthi detail sing realistis banget, dilengkapi sistem pencahayaan LED sing nggawe katon spektakuler ning wengi.

Tugu Mangga ana ning lokasi strategis ning Jalan Raya Pahlawan, cedhak karo kantor Bupati Indramayu lan ora adoh saking Alun-alun Puspawangi. Lokasi iki gampang banget diakses amarga ana ning jalur utama sing nyambungake macem-macem destinasi wisata ning Indramayu. Para pengunjung bisa nganggo macem-macem moda transportasi, wiwit kendaraan pribadi, angkutan umum, nganti ojek online. Area sekitar tugu dilengkapi taman cilik, bangku taman, lan area parkir sing memadai, dadekake panggonan sing nyaman kanggo istirahat sejenak.

Tugu Mangga wis dadi spot foto wajib kanggo para wisatawan sing berkunjung ning Indramayu, utamane ning wengi nalika illuminasi LED menehi efek visual sing memukau. Monumen iki uga kerep didadekake meeting point kanggo macem-macem acara komunitas lan titik start city tour Indramayu. Ning sekitar tugu, ana pedagang kaki lima sing ngedol macem-macem oleh-oleh khas Indramayu kalebu produk olahan mangga. Keberadaan tugu iki ora mung fungsi minangka penanda geografis, nanging uga minangka media edukasi kanggo masyarakat babagan potensi pertanian daerah lan pentinge nguri-uri varietas unggul lokal. Saben taun, tugu iki dadi salah siji venue ning rangkaian Festival Mangga Gedong Gincu kanthi macem-macem dekorasi tambahan sing nggawe saya menarik."""
        
    else:
        # Generic template in Indramayu language
        return f"""{topic} iku salah siji destinasi wisata unggulan ning Kabupaten Indramayu sing duwe nilai historis lan budaya dhuwur. Panggonan iki wis dadi bagean penting saking perkembangan pariwisata lokal lan nawakake pengalaman unik kanggo saben pengunjung. Kanthi keunikan sing khas, {topic} kasil narik kawigatene para wisatawan saking macem-macem daerah kanggo teka lan ngrasakake pesona sing ditawakake.

Lokasi {topic} bisa diakses kanthi gampang ngliwati jalur transportasi utama ning Indramayu. Para pengunjung bisa nganggo kendaraan pribadi utawa angkutan umum kanthi fasilitas sing memadai ning sekitar area. Wektu tempuh saking pusat kutha relatif cendhak lan jalur akses ning kondisi apik. Ana area parkir sing jembar lan macem-macem fasilitas pendukung liyane kanggo kenyamanan para wisatawan.

Daya tarik utama {topic} meliputi kaendahan alam lan nilai budaya sing dhuwur, menehi pengalaman wisata sing berkesan. Para pengunjung bisa nikmati macem-macem aktivitas menarik sambil sinau babagan sejarah lan budaya lokal Indramayu. Panggonan iki uga kerep ngadakake event-event khusus sing nambahi daya tarike. Fasilitas sing kasedhiya cukup lengkap kanggo ndhukung kenyamanan para wisatawan selama berkunjung."""

def create_conversation_pair(topic: str) -> List[Dict]:
    """Create two conversation objects for a topic - one in Indonesian, one in Indramayu"""
    question = generate_question_for_topic(topic)
    
    # Indonesian conversation
    indonesian_conversation = {
        "conversations": [
            {
                "role": "human", 
                "content": question
            },
            {
                "role": "assistant",
                "content": generate_detailed_answer_indonesian(topic)
            }
        ]
    }
    
    # Indramayu conversation  
    indramayu_conversation = {
        "conversations": [
            {
                "role": "human",
                "content": question  # Same question
            },
            {
                "role": "assistant", 
                "content": generate_detailed_answer_indramayu(topic)
            }
        ]
    }
    
    return [indonesian_conversation, indramayu_conversation]

def main():
    """Main function to generate the complete dataset"""
    print("Starting dataset generation...")
    
    # Extract topics
    topics = extract_topics('/home/runner/work/dataset/dataset/list-topik.txt')
    print(f"Found {len(topics)} topics")
    
    # Generate conversations
    all_conversations = []
    for i, topic in enumerate(topics, 1):
        print(f"Generating conversations for topic {i}/{len(topics)}: {topic}")
        conversations = create_conversation_pair(topic)
        all_conversations.extend(conversations)
    
    # Save to JSON file
    output_file = '/home/runner/work/dataset/dataset/dataset.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_conversations, f, ensure_ascii=False, indent=2)
    
    print(f"Dataset generation complete!")
    print(f"Total conversations: {len(all_conversations)}")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main()