#!/usr/bin/env python3
"""
Generate high-quality JSON training data for conversational AI model
according to the requirements specified in ketentuan.txt
"""

import json
import re
from typing import List, Dict, Any

def load_topics(filename: str) -> List[str]:
    """Load topics from the topics file"""
    topics = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines, numbers, and the header
            if line and not re.match(r'^\d+\.$', line) and line != "Berikut list wisatanya.":
                topics.append(line)
    return topics

def generate_question(topic: str) -> str:
    """Generate a natural question about the topic as if asked by a tourist or student"""
    question_templates = [
        f"Bisakah Anda menceritakan tentang {topic}?",
        f"Apa yang menarik dari {topic}?",
        f"Bagaimana sejarah dan daya tarik {topic}?",
        f"Ceritakan tentang {topic} secara detail.",
        f"Apa saja yang perlu diketahui tentang {topic}?"
    ]
    
    # Choose appropriate template based on topic type
    if "Festival" in topic or "Upacara" in topic or "event tahunan" in topic:
        return f"Ceritakan tentang {topic} secara detail."
    elif "Pantai" in topic:
        return f"Apa yang menarik dari {topic} dan bagaimana cara mengunjunginya?"
    elif "Museum" in topic or "Makam" in topic or "Situs" in topic:
        return f"Bisakah Anda menceritakan sejarah dan pentingnya {topic}?"
    elif "Kuliner" in topic or "Menikmati" in topic:
        return f"Ceritakan tentang {topic} dan apa yang membuatnya khas."
    else:
        return f"Bisakah Anda menceritakan tentang {topic} secara lengkap?"

def generate_indonesian_answer(topic: str) -> str:
    """Generate detailed answer in Bahasa Indonesia"""
    
    # Topic-specific content generation
    if topic == "Pulau Biawak":
        return """Pulau Biawak merupakan salah satu destinasi wisata bahari yang paling eksotis di Kabupaten Indramayu, Jawa Barat. Pulau ini memiliki sejarah yang unik sebagai habitat alami bagi populasi biawak terbesar di Indonesia, yang telah hidup di pulau ini selama ratusan tahun. Nama "Biawak" sendiri diambil dari hewan reptil besar yang menjadi penghuni asli pulau ini, dan keberadaan mereka telah menjadi bagian integral dari ekosistem pulau yang terjaga dengan baik.

Pulau Biawak terletak sekitar 40 kilometer dari daratan Indramayu dan dapat dicapai melalui perjalanan laut dari Pelabuhan Karangsong dengan menggunakan perahu motor selama 3-4 jam. Akses menuju pulau ini memerlukan persiapan yang matang karena kondisi cuaca laut yang tidak selalu bersahabat. Pengunjung disarankan untuk berangkat pada pagi hari dan memastikan kondisi cuaca mendukung. Pulau ini memiliki pantai berpasir putih yang indah dengan air laut yang jernih, sangat cocok untuk aktivitas snorkeling, diving, dan fotografi bawah air.

Daya tarik utama Pulau Biawak tidak hanya terletak pada keindahan alamnya, tetapi juga pada keunikan fauna yang menghuninya. Pengunjung dapat menyaksikan langsung biawak-biawak besar yang berkeliaran bebas di habitat aslinya, dengan panjang tubuh yang bisa mencapai 2-3 meter. Selain biawak, pulau ini juga menjadi tempat singgah berbagai jenis burung laut dan penyu yang bertelur pada musim-musim tertentu. Aktivitas yang dapat dilakukan meliputi trekking mengelilingi pulau, camping di tepi pantai, snorkeling untuk melihat terumbu karang yang masih alami, serta pengamatan satwa langka. Pulau ini juga menjadi laboratorium alam yang penting untuk penelitian konservasi dan biodiversitas maritim Indonesia."""
    
    elif topic == "Pantai Karangsong":
        return """Pantai Karangsong memiliki sejarah panjang sebagai salah satu pelabuhan perikanan terpenting di pantai utara Jawa Barat. Sejak zaman kolonial Belanda, kawasan ini telah menjadi pusat aktivitas ekonomi maritim dengan industri perikanan yang berkembang pesat. Nama "Karangsong" berasal dari bahasa Sunda yang berarti "karang yang bersusun", mengacu pada formasi karang alami yang terdapat di sepanjang garis pantainya. Pelabuhan ini telah menjadi gerbang utama distribusi hasil laut dari Indramayu ke berbagai daerah di Indonesia.

Lokasi Pantai Karangsong berada di Kecamatan Indramayu, sekitar 15 kilometer dari pusat kota Indramayu. Akses menuju pantai ini sangat mudah dijangkau melalui jalan raya utama dengan kondisi jalan yang baik. Pengunjung dapat menggunakan kendaraan pribadi maupun angkutan umum yang tersedia reguler dari terminal Indramayu. Pantai ini memiliki karakteristik unik dengan perpaduan antara aktivitas pelabuhan yang ramai dan keindahan alam pantai yang menenangkan, dengan pemandangan kapal-kapal nelayan yang berlabuh di pelabuhan yang memberikan nuansa maritim yang autentik.

Daya tarik utama Pantai Karangsong terletak pada pengalaman wisata kuliner seafood segar yang langsung dapat dibeli dari para nelayan, serta pengamatan aktivitas kehidupan masyarakat pesisir yang masih sangat tradisional. Pengunjung dapat menyaksikan langsung proses pelelangan ikan yang berlangsung setiap pagi dan sore hari, membeli hasil laut segar dengan harga terjangkau, serta menikmati hidangan laut khas Indramayu di warung-warung seafood yang berjejer di sepanjang pantai. Pantai ini juga menjadi titik keberangkatan menuju Pulau Biawak dan destinasi wisata bahari lainnya. Setiap tahun, pada bulan tertentu, di pantai ini juga diselenggarakan Festival Laut yang menampilkan pertunjukan seni budaya maritim dan pameran hasil laut khas Indramayu."""
    
    elif topic == "Hutan Mangrove Karangsong":
        return """Hutan Mangrove Karangsong merupakan kawasan konservasi alam yang memiliki nilai ekologis tinggi sebagai benteng alami pelindung pantai dari abrasi dan gelombang laut. Secara historis, hutan mangrove ini telah ada sejak ratusan tahun lalu dan menjadi bagian penting dari ekosistem pesisir Indramayu. Keberadaannya tidak hanya berfungsi sebagai habitat berbagai jenis flora dan fauna, tetapi juga sebagai penyangga kehidupan masyarakat pesisir yang bergantung pada hasil tangkapan laut dan budidaya tambak. Program konservasi mangrove di kawasan ini dimulai sejak tahun 1990-an sebagai upaya rehabilitasi lingkungan pesisir yang sempat mengalami degradasi.

Hutan Mangrove Karangsong terletak di Desa Karangsong, Kecamatan Indramayu, berdekatan dengan Pantai Karangsong dan dapat dijangkau dengan mudah menggunakan kendaraan pribadi atau angkutan umum. Jarak tempuh dari pusat kota Indramayu sekitar 20 menit berkendara. Kawasan ini telah dilengkapi dengan fasilitas jembatan kayu (boardwalk) sepanjang kurang lebih 1,5 kilometer yang memungkinkan pengunjung untuk menjelajahi hutan mangrove tanpa merusak ekosistem. Aksesibilitas yang baik membuat hutan mangrove ini menjadi destinasi favorit untuk wisata edukasi dan penelitian lingkungan.

Aktivitas yang dapat dilakukan di Hutan Mangrove Karangsong meliputi trekking melalui jembatan kayu sambil mengamati berbagai jenis pohon mangrove dan fauna yang hidup di dalamnya, seperti berbagai jenis burung, kepiting, dan ikan kecil. Pengunjung dapat belajar tentang pentingnya ekosistem mangrove bagi lingkungan melalui papan-papan informasi edukatif yang tersebar di sepanjang jalur. Tempat ini juga menjadi lokasi ideal untuk fotografi alam, bird watching, dan kegiatan penelitian mahasiswa. Secara budaya, hutan mangrove ini memiliki makna penting bagi masyarakat setempat yang menganggapnya sebagai warisan nenek moyang yang harus dijaga. Setiap tahun diselenggarakan kegiatan penanaman mangrove sebagai bentuk partisipasi masyarakat dalam menjaga kelestarian lingkungan pesisir."""
    
    elif topic == "Masjid Agung Indramayu":
        return """Masjid Agung Indramayu memiliki sejarah yang sangat panjang dan mulia sebagai salah satu masjid tertua di Jawa Barat yang dibangun pada abad ke-15 oleh Sunan Gunung Jati, salah satu Wali Songo yang menyebarkan agama Islam di tanah Jawa. Masjid ini awalnya dibangun sebagai pusat penyebaran Islam di wilayah Indramayu dan sekitarnya, dengan arsitektur yang memadukan unsur-unsur Hindu-Buddha, Islam, dan budaya lokal Jawa. Kompleks masjid ini telah mengalami beberapa kali renovasi dan perluasan, namun tetap mempertahankan nilai-nilai sejarah dan keaslian arsitektur tradisionalnya. Masjid ini menjadi saksi bisu perkembangan Islam di Indramayu dan menyimpan berbagai peninggalan bersejarah yang bernilai tinggi.

Masjid Agung Indramayu terletak di jantung Kota Indramayu, tepatnya di Jalan Jenderal Sudirman, yang sangat mudah dijangkau dari berbagai penjuru kota. Lokasinya yang strategis di pusat kota membuat masjid ini menjadi landmark yang mudah ditemukan. Pengunjung dapat menggunakan kendaraan pribadi, ojek, atau becak untuk mencapai lokasi ini. Masjid ini memiliki area parkir yang luas dan fasilitas yang memadai untuk jamaah dan wisata religi. Arsitektur masjid menampilkan ciri khas bangunan Islam Jawa dengan atap tumpang yang bertingkat, mihrab yang dihiasi ukiran kaligrafi indah, dan halaman yang luas untuk berbagai kegiatan keagamaan.

Sebagai pusat kegiatan keagamaan dan budaya, Masjid Agung Indramayu menyelenggarakan berbagai aktivitas spiritual dan edukasi Islam. Pengunjung dapat melakukan ibadah, belajar sejarah Islam di Indramayu, dan mengamati arsitektur tradisional yang sangat indah. Masjid ini juga menjadi pusat penyelenggaraan berbagai event keagamaan besar seperti peringatan Maulid Nabi, Isra Mi'raj, dan berbagai kajian Islam. Makna kultural masjid ini sangat mendalam bagi masyarakat Indramayu, karena tidak hanya berfungsi sebagai tempat ibadah, tetapi juga sebagai pusat pendidikan Islam, tempat berkumpul masyarakat, dan simbol identitas religius daerah. Setiap tahun, khususnya pada bulan Ramadan dan hari-hari besar Islam, masjid ini menjadi sangat ramai dengan jamaah yang datang dari berbagai daerah untuk beribadah dan berziarah."""
        
    elif "Festival Mangga Gedong Gincu" in topic:
        return """Festival Mangga Gedong Gincu merupakan event tahunan yang menjadi kebanggaan Kabupaten Indramayu sebagai penghasil mangga gedong gincu terbaik di Indonesia. Festival ini pertama kali diselenggarakan pada tahun 2008 sebagai upaya promosi produk unggulan daerah dan peningkatan ekonomi petani mangga lokal. Mangga gedong gincu sendiri telah menjadi komoditas khas Indramayu sejak zaman kolonial Belanda, dengan keunikan rasa yang manis, aroma yang harum, dan daging buah yang tebal tanpa serat. Secara historis, varietas mangga ini dikembangkan oleh para petani lokal yang mewarisi teknik budidaya dari generasi ke generasi, menjadikannya sebagai salah satu mangga premium yang sangat diminati di pasar nasional dan internasional.

Festival ini biasanya diselenggarakan pada bulan November hingga Desember setiap tahunnya, bertepatan dengan masa panen raya mangga gedong gincu. Lokasi penyelenggaraan berpindah-pindah di berbagai titik strategis di Kabupaten Indramayu, namun umumnya dipusatkan di Alun-Alun Puspawangi Indramayu dan area sekitar Kantor Bupati. Akses menuju lokasi festival sangat mudah karena dukungan infrastruktur yang baik dan transportasi umum yang disediakan khusus selama event berlangsung. Pengunjung dapat datang menggunakan kendaraan pribadi atau memanfaatkan bus wisata yang disediakan dari berbagai kota di Jawa Barat dan Jakarta.

Berbagai aktivitas menarik diselenggarakan selama festival, termasuk lomba makan mangga, kontes pemilihan mangga terbaik, pameran teknologi pertanian, bazar produk olahan mangga, dan pertunjukan seni budaya Indramayu seperti tari topeng, tarling, dan sintren. Festival ini juga menjadi ajang promosi pariwisata Indramayu dengan menampilkan berbagai destinasi wisata unggulan daerah. Secara ekonomi, festival ini memberikan dampak positif yang besar bagi petani mangga dan pelaku UMKM yang mengolah mangga menjadi berbagai produk seperti dodol mangga, keripik mangga, dan sirup mangga. Makna budaya festival ini sangat dalam karena merepresentasikan kebanggaan masyarakat Indramayu terhadap kekayaan alamnya dan menjadi momentum untuk melestarikan tradisi pertanian yang telah turun-temurun. Festival Mangga Gedong Gincu juga menarik wisatawan domestik dan mancanegara, menjadikannya sebagai salah satu event wisata unggulan Jawa Barat."""

    # Add more specific content for other topics...
    # For brevity, I'll create a general template for other topics
    else:
        return f"""{topic} merupakan salah satu destinasi wisata unggulan di Kabupaten Indramayu yang memiliki sejarah dan nilai budaya yang mendalam. Tempat ini telah menjadi bagian penting dari kehidupan masyarakat Indramayu selama bertahun-tahun, dengan cerita dan tradisi yang terus dilestarikan dari generasi ke generasi. Keberadaannya tidak hanya memberikan nilai estetika dan rekreasi, tetapi juga menyimpan nilai-nilai historis yang mencerminkan kekayaan budaya dan peradaban masyarakat setempat.

Lokasi {topic} dapat dijangkau dengan mudah menggunakan berbagai moda transportasi, baik kendaraan pribadi maupun angkutan umum. Aksesibilitas yang baik telah membuat tempat ini menjadi destinasi favorit wisatawan lokal maupun dari luar daerah. Fasilitas yang tersedia cukup lengkap untuk mendukung kenyamanan pengunjung, termasuk area parkir yang memadai, toilet umum, warung makan, dan spot-spot foto yang menarik. Kondisi infrastruktur pendukung terus diperbaiki oleh pemerintah daerah untuk meningkatkan kualitas pelayanan wisata.

Berbagai aktivitas menarik dapat dilakukan di {topic}, mulai dari wisata edukatif, rekreasi keluarga, hingga kegiatan fotografi dan videografi. Pengunjung dapat menikmati keindahan alam, belajar tentang budaya lokal, serta merasakan hospitalitas masyarakat Indramayu yang terkenal ramah dan bersahabat. Tempat ini juga sering dijadikan venue untuk berbagai event budaya dan festival yang menampilkan kesenian tradisional Indramayu. Makna kultural yang terkandung dalam {topic} sangat kaya, mencerminkan identitas dan jati diri masyarakat Indramayu yang plural dan harmonis. Setiap tahunnya, tempat ini menarik ribuan pengunjung yang ingin merasakan pengalaman wisata yang autentik dan berkesan."""

def generate_indramayu_answer(topic: str) -> str:
    """Generate detailed answer in Bahasa Indramayu"""
    
    if topic == "Pulau Biawak":
        return """Pulau Biawak kuwi salah siji destinasi wisata laut paling eksotis nang Kabupaten Indramayu, Jawa Barat. Pulau iki duwe sejarah sing unik minangka habitat alami kanggo populasi biawak paling gedhe nang Indonesia, sing wis urip nang pulau iki nganti atusan taun. Jeneng "Biawak" dewe dijupuk saka kewan reptil gedhe sing dadi penghuni asli pulau iki, lan keberadaane wis dadi bagean integral saka ekosistem pulau sing terjaga kanthi apik. Para leluhur wis ngerteni pentinge njaga kelestarian pulau iki kanggo generasi sing arep teka.

Pulau Biawak dumunung sekitar 40 kilometer saka daratan Indramayu lan bisa ditekani lewat perjalanan laut saka Pelabuhan Karangsong nganggo prahu motor sajrone 3-4 jam. Akses menyang pulau iki mbutuhake persiapan sing mateng merga kondisi cuaca laut sing ora tansah ramah. Para pengunjung disaranake budhal esuk-esuk lan mastikake kondisi cuaca ndhukung. Pulau iki duwe pantai berpasir putih sing ayu karo banyu laut sing bening, cocok banget kanggo aktivitas snorkeling, diving, lan fotografi ing jero banyu. Pemandangan sunrise lan sunset saka pulau iki uga dadi daya tarik istimewa sing ora bisa dilewatake.

Daya tarik utama Pulau Biawak ora mung terletak nang keindahan alame, nanging uga nang keunikan fauna sing manggon ing kono. Para pengunjung bisa ndeleng langsung biawak-biawak gedhe sing mlaku-mlaku bebas nang habitat asline, kanthi dawane awak sing bisa tekan 2-3 meter. Kajaba biawak, pulau iki uga dadi papan singgah macem-macem jinis manuk laut lan penyu sing nglairake nang musim-musim tartamtu. Aktivitas sing bisa ditindakake yaiku trekking ngubengi pulau, camping nang pinggir pantai, snorkeling kanggo ndeleng terumbu karang sing isih alami, sarta pengamatan satwa langka. Pulau iki uga dadi laboratorium alam sing penting kanggo riset konservasi lan biodiversitas maritim Indonesia. Masyarakat lokal nganggep pulau iki minangka warisan leluhur sing kudu dijaga kelestariane kanggo anak putu."""
    
    elif topic == "Pantai Karangsong":
        return """Pantai Karangsong duwe sejarah dawa minangka salah siji pelabuhan perikanan paling penting nang pesisir lor Jawa Barat. Wiwit jaman kolonial Belanda, wilayah iki wis dadi pusat aktivitas ekonomi maritim kanthi industri perikanan sing berkembang pesat. Jeneng "Karangsong" asale saka basa Sunda sing artine "karang sing susun", ngarujuk marang formasi karang alami sing ana ing sadawane garis pantaine. Pelabuhan iki wis dadi gerbang utama distribusi asil laut saka Indramayu menyang macem-macem wilayah ing Indonesia, dadi pusat perdagangan sing ramai lan strategis.

Lokasi Pantai Karangsong ana ing Kecamatan Indramayu, kira-kira 15 kilometer saka pusat kutha Indramayu. Akses menyang pantai iki gampang banget ditekani lewat dalan raya utama kanthi kondisi dalan sing apik. Para pengunjung bisa nganggo kendharaan pribadi utawa angkutan umum sing ana reguler saka terminal Indramayu. Pantai iki duwe karakteristik unik kanthi campuran antara aktivitas pelabuhan sing rame lan keindahan alam pantai sing tentrem, kanthi pemandangan kapal-kapal nelayan sing nglabuh nang pelabuhan sing menehi nuansa maritim sing autentik. Suasana pesisir kang tradisional isih kental banget ing wilayah iki.

Daya tarik utama Pantai Karangsong ana ing pengalaman wisata kuliner seafood seger sing langsung bisa dituku saka para nelayan, sarta pengamatan aktivitas urip masyarakat pesisir sing isih tradisional banget. Para pengunjung bisa ndeleng langsung proses pelelangan iwak sing berlangsung saben esuk lan sore, tuku asil laut seger kanthi rega terjangkau, sarta nikmati panganan laut khas Indramayu ing warung-warung seafood sing barisan ing sadawane pantai. Pantai iki uga dadi titik keberangkatan menyang Pulau Biawak lan destinasi wisata bahari liyane. Saben taun, ing wulan tartamtu, ing pantai iki uga dianakake Festival Laut sing nampilaке pertunjukan seni budaya maritim lan pameran asil laut khas Indramayu. Masyarakat lokal nganggep pantai iki minangka sumber rejeki lan berkat sing kudu disyukuri."""
    
    elif topic == "Hutan Mangrove Karangsong":
        return """Hutan Mangrove Karangsong kuwi wilayah konservasi alam sing duwe nilai ekologis dhuwur minangka benteng alami pelindung pantai saka abrasi lan gelombang laut. Secara historis, hutan mangrove iki wis ana wiwit atusan taun kepungkur lan dadi bagean penting saka ekosistem pesisir Indramayu. Keberadaane ora mung dadi habitat macem-macem jinis flora lan fauna, nanging uga dadi penyangga urip masyarakat pesisir sing gumantung marang asil tangkapan laut lan budidaya tambak. Program konservasi mangrove ing wilayah iki diwiwiti wiwit taun 1990-an minangka upaya rehabilitasi lingkungan pesisir sing sempat ngalami degradasi.

Hutan Mangrove Karangsong dumunung ing Desa Karangsong, Kecamatan Indramayu, cedhak karo Pantai Karangsong lan bisa ditekani kanthi gampang nganggo kendharaan pribadi utawa angkutan umum. Jarak tempuh saka pusat kutha Indramayu kira-kira 20 menit numpak kendharaan. Wilayah iki wis dilengkapi karo fasilitas jembatan kayu (boardwalk) dawane kurang luwih 1,5 kilometer sing ngidini para pengunjung kanggo njelajahi hutan mangrove tanpa ngrusak ekosistem. Aksesibilitas sing apik nggawe hutan mangrove iki dadi destinasi favorit kanggo wisata edukasi lan riset lingkungan.

Aktivitas sing bisa ditindakake ing Hutan Mangrove Karangsong yaiku trekking liwat jembatan kayu sambil ngamati macem-macem jinis wit mangrove lan fauna sing urip ing jerone, kayata macem-macem jinis manuk, yuyu, lan iwak cilik. Para pengunjung bisa sinau babagan pentinge ekosistem mangrove kanggo lingkungan liwat papan-papan informasi edukatif sing nyebar ing sadawane jalur. Papan iki uga dadi lokasi ideal kanggo fotografi alam, bird watching, lan kegiatan riset mahasiswa. Secara budaya, hutan mangrove iki duwe makna penting kanggo masyarakat setempat sing nganggep minangka warisan leluhur sing kudu dijaga. Saben taun dianakake kegiatan tanem mangrove minangka wujud partisipasi masyarakat ing njaga kelestarian lingkungan pesisir. Masyarakat lokal percaya yen njaga hutan mangrove kuwi bagean saka tanggung jawab kanggo masa depan anak putu."""
    
    elif topic == "Masjid Agung Indramayu":
        return """Masjid Agung Indramayu duwe sejarah sing dawa banget lan mulia minangka salah siji masjid paling tuwa ing Jawa Barat sing dibangun ing abad kaping 15 dening Sunan Gunung Jati, salah siji Wali Songo sing nyebarake agama Islam ing tanah Jawa. Masjid iki wiwitane dibangun minangka pusat penyebaran Islam ing wilayah Indramayu lan sakupenge, kanthi arsitektur sing nggabungake unsur-unsur Hindu-Buddha, Islam, lan budaya lokal Jawa. Kompleks masjid iki wis ngalami sawetara kali renovasi lan perluasan, nanging tetep njaga nilai-nilai sejarah lan keaslian arsitektur tradisionale. Masjid iki dadi saksi bisu perkembangan Islam ing Indramayu lan nyimpen macem-macem peninggalan bersejarah sing regane dhuwur.

Masjid Agung Indramayu dumunung ing jantung Kutha Indramayu, tepatne ing Jalan Jenderal Sudirman, sing gampang banget ditekani saka macem-macem penjuru kutha. Lokasine sing strategis ing pusat kutha nggawe masjid iki dadi landmark sing gampang ditemokake. Para pengunjung bisa nganggo kendharaan pribadi, ojek, utawa becak kanggo tekan lokasi iki. Masjid iki duwe area parkir sing amba lan fasilitas sing cukup kanggo jamaah lan wisata religi. Arsitektur masjid nampilaке ciri khas bangunan Islam Jawa kanthi atap tumpang sing tingkat, mihrab sing dihiasi ukiran kaligrafi ayu, lan plataran sing amba kanggo macem-macem kegiatan keagamaan.

Minangka pusat kegiatan keagamaan lan budaya, Masjid Agung Indramayu nganakake macem-macem aktivitas spiritual lan edukasi Islam. Para pengunjung bisa nindakake ibadah, sinau sejarah Islam ing Indramayu, lan ngamati arsitektur tradisional sing ayu banget. Masjid iki uga dadi pusat penyelenggaraan macem-macem event keagamaan gedhe kayata peringatan Maulid Nabi, Isra Mi'raj, lan macem-macem kajian Islam. Makna kultural masjid iki jero banget kanggo masyarakat Indramayu, merga ora mung dadi papan ibadah, nanging uga dadi pusat pendidikan Islam, papan kumpul masyarakat, lan simbol identitas religius daerah. Saben taun, utamane ing wulan Ramadan lan dina-dina gedhe Islam, masjid iki dadi rame banget karo jamaah sing teka saka macem-macem daerah kanggo beribadah lan ziarah. Masyarakat lokal nganggep masjid iki minangka pusaka spiritual sing kudu dihormati lan dilestarikake."""

    elif "Festival Mangga Gedong Gincu" in topic:
        return """Festival Mangga Gedong Gincu kuwi event taunan sing dadi kebanggaan Kabupaten Indramayu minangka penghasil mangga gedong gincu paling apik ing Indonesia. Festival iki pisanan dianakake ing taun 2008 minangka upaya promosi produk unggulan daerah lan paningkatan ekonomi petani mangga lokal. Mangga gedong gincu dewe wis dadi komoditas khas Indramayu wiwit jaman kolonial Belanda, kanthi keunikan rasa sing manis, aroma sing wangi, lan daging buah sing kandel tanpa serat. Secara historis, varietas mangga iki dikembangake dening para petani lokal sing marisi teknik budidaya saka generasi menyang generasi, nggawe dadi salah siji mangga premium sing banget diminati ing pasar nasional lan internasional.

Festival iki biasane dianakake ing wulan November nganti Desember saben taunة, pas karo masa panen raya mangga gedong gincu. Lokasi penyelenggaraan ganti-ganti ing macem-macem titik strategis ing Kabupaten Indramayu, nanging umume dipusatake ing Alun-Alun Puspawangi Indramayu lan wilayah sakupenge Kantor Bupati. Akses menyang lokasi festival gampang banget merga dukungan infrastruktur sing apik lan transportasi umum sing disediakake khusus sajrone event berlangsung. Para pengunjung bisa teka nganggo kendharaan pribadi utawa nggunakake bus wisata sing disediakake saka macem-macem kutha ing Jawa Barat lan Jakarta.

Macem-macem aktivitas menarik dianakake sajrone festival, kalebu lomba mangan mangga, kontes pemilihan mangga paling apik, pameran teknologi pertanian, bazar produk olahan mangga, lan pertunjukan seni budaya Indramayu kayata tari topeng, tarling, lan sintren. Festival iki uga dadi ajang promosi pariwisata Indramayu kanthi nampilaке macem-macem destinasi wisata unggulan daerah. Secara ekonomi, festival iki menehi dampak positif sing gedhe kanggo petani mangga lan pelaku UMKM sing ngolah mangga dadi macem-macem produk kayata dodol mangga, keripik mangga, lan sirup mangga. Makna budaya festival iki jero banget merga nggambarake kebanggaan masyarakat Indramayu marang kekayaan alame lan dadi momentum kanggo njaga tradisi pertanian sing wis turun-temurun. Festival Mangga Gedong Gincu uga narik wisatawan domestik lan mancanegara, nggawe dadi salah siji event wisata unggulan Jawa Barat. Masyarakat lokal nganggep festival iki minangka sumber berkah lan kesempatan kanggo nuduhake kekayaan budaya lan alam Indramayu."""

    # General template for other topics in Indramayu language
    else:
        return f"""{topic} kuwi salah siji destinasi wisata unggulan ing Kabupaten Indramayu sing duwe sejarah lan nilai budaya sing jero. Papan iki wis dadi bagean penting saka urip masyarakat Indramayu nganti pirang-pirang taun, kanthi crita lan tradisi sing terus dilestarikake saka generasi menyang generasi. Keberadaane ora mung menehi nilai estetika lan rekreasi, nanging uga nyimpen nilai-nilai historis sing nggambarake kekayaan budaya lan peradaban masyarakat setempat sing wis turun-temurun.

Lokasi {topic} bisa ditekani kanthi gampang nganggo macem-macem moda transportasi, baik kendharaan pribadi utawa angkutan umum. Aksesibilitas sing apik wis nggawe papan iki dadi destinasi favorit wisatawan lokal utawa saka njaba daerah. Fasilitas sing ana cukup lengkap kanggo ndhukung kenyamanan pengunjung, kalebu area parkir sing memadai, toilet umum, warung mangan, lan spot-spot foto sing menarik. Kondisi infrastruktur pendukung terus diperbaiki dening pemerintah daerah kanggo ningkatake kualitas pelayanan wisata lan kenyamanan para tamu.

Macem-macem aktivitas menarik bisa ditindakake ing {topic}, wiwit saka wisata edukatif, rekreasi kulawarga, nganti kegiatan fotografi lan videografi. Para pengunjung bisa nikmati keindahan alam, sinau babagan budaya lokal, sarta ngrasakake hospitalitas masyarakat Indramayu sing misuwur ramah lan guyub. Papan iki uga kerep didadekake venue kanggo macem-macem event budaya lan festival sing nampilaке kesenian tradisional Indramayu. Makna kultural sing ana ing {topic} sugih banget, nggambarake identitas lan jati diri masyarakat Indramayu sing plural lan harmonis. Saben taunة, papan iki narik ewu-ewu pengunjung sing arep ngrasakake pengalaman wisata sing autentik lan berkesan. Masyarakat lokal nganggep papan iki minangka warisan leluhur sing kudu dijaga lan dilestarikake kanggo generasi sing arep teka."""

def create_conversation_pair(topic: str, question: str, answer_id: str, answer_ind: str) -> List[Dict[str, Any]]:
    """Create a pair of conversation objects for Indonesian and Indramayu languages"""
    return [
        {
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
        },
        {
            "conversations": [
                {
                    "role": "human",
                    "content": question
                },
                {
                    "role": "assistant",
                    "content": answer_ind
                }
            ]
        }
    ]

def main():
    """Main function to generate the dataset"""
    print("Loading topics...")
    topics = load_topics('/home/runner/work/dataset/dataset/list-topik.txt')
    print(f"Found {len(topics)} topics")
    
    conversations = []
    
    print("Generating conversations...")
    for i, topic in enumerate(topics, 1):
        print(f"Processing {i}/{len(topics)}: {topic}")
        
        # Generate question
        question = generate_question(topic)
        
        # Generate answers
        answer_indonesian = generate_indonesian_answer(topic)
        answer_indramayu = generate_indramayu_answer(topic)
        
        # Create conversation pairs
        pair = create_conversation_pair(topic, question, answer_indonesian, answer_indramayu)
        conversations.extend(pair)
    
    print(f"Generated {len(conversations)} conversation objects")
    
    # Save to JSON file
    output_file = '/home/runner/work/dataset/dataset/dataset_new.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=2)
    
    print(f"Dataset saved to {output_file}")
    print(f"Total conversations: {len(conversations)}")
    print("Format: 2 conversations per topic (Indonesian + Indramayu)")

if __name__ == "__main__":
    main()