# Indramayu Tourism Dataset for Conversational AI

This repository contains a high-quality JSON dataset for training conversational AI models with focus on Indramayu tourism information in both Bahasa Indonesia and Bahasa Indramayu.

## Dataset Overview

- **Total Conversations**: 68 conversation objects
- **Topics Covered**: 34 tourism destinations and cultural experiences in Indramayu
- **Languages**: Bahasa Indonesia (34 answers) and Bahasa Indramayu (34 answers)
- **Format**: JSON array following conversational AI training format

## Dataset Structure

Each conversation object follows this structure:
```json
{
  "conversations": [
    {
      "role": "human",
      "content": "<question about Indramayu tourism>"
    },
    {
      "role": "assistant", 
      "content": "<detailed answer in Indonesian or Indramayu>"
    }
  ]
}
```

## Content Quality Standards

Each answer includes **3+ paragraphs** covering:
- **Historical background** of the destination/cultural experience
- **Location and access information** (how to get there, transportation)
- **Main attractions and activities** available
- **Cultural or historical significance** to local community
- **Festivals or special events** (when applicable)

## Topics Covered

### Natural Attractions
- Pulau Biawak (Biawak Island)
- Pantai Karangsong (Karangsong Beach)
- Hutan Mangrove Karangsong (Karangsong Mangrove Forest)
- Pantai Tirtamaya, Pantai Balongan Indah, and other beaches
- Situ Bolang, Situ Bojongsari, Situ Gede (various lakes)

### Cultural & Historical Sites
- Masjid Agung Indramayu (Grand Mosque)
- Makam Raden Arya Wiralodra (Historical tomb)
- Situs Buyut Banjar (Archaeological site)
- Museum Badak Putih (White Rhino Museum)
- Monumen Perjuangan (Struggle Monument)

### Recreation & Entertainment
- Multiple waterparks (Waterboom Bojongsari, Tiga Bintang Firdaus, etc.)
- Alun-Alun Puspawangi Indramayu (Main square)
- Taman Kehati Indramayu (Biodiversity park)

### Culinary & Cultural Experiences
- Traditional food experiences (Nasi Lengko, Burbacek, Rumbah)
- Culinary centers (Pindang Gombyang, seafood processing)
- Cultural events (Upacara Adat Nadran, Festival Mangga Gedong Gincu)

## Language Features

### Bahasa Indonesia
- Formal Indonesian language
- Rich vocabulary and varied sentence structures
- Cultural sensitivity and local context

### Bahasa Indramayu  
- Authentic local dialect of Indramayu region
- Traditional expressions and local terminology
- Cultural authenticity maintained

## Files

- `dataset.json` - Main dataset file with 68 conversation objects
- `list-topik.txt` - Original list of 34 tourism topics
- `ketentuan.txt` - Requirements and quality standards (Indonesian)
- `generate_dataset.py` - Python script used to generate the dataset
- `validate_dataset.py` - Validation script to verify dataset quality
- `dataset_old.json` - Previous dataset (archived)

## Usage

This dataset can be used for:
- Training conversational AI models for tourism information
- Fine-tuning language models for Indonesian and Indramayu languages
- Research on multilingual AI systems
- Cultural heritage preservation through AI
- Tourism chatbot development

## Quality Assurance

The dataset has been validated for:
- ✅ JSON structure correctness
- ✅ Complete topic coverage (34/34 topics)
- ✅ Language distribution balance (34 Indonesian + 34 Indramayu)
- ✅ Answer depth (all answers have 3+ substantive paragraphs)
- ✅ Content quality and authenticity
- ✅ Cultural sensitivity and accuracy

## Generation Methodology

1. **Topic Extraction**: Parsed 34 unique tourism topics from `list-topik.txt`
2. **Question Generation**: Created natural, tourist-appropriate questions for each topic
3. **Content Development**: Generated detailed, informative answers covering all required aspects
4. **Language Implementation**: Provided authentic translations/adaptations in both languages
5. **Quality Control**: Ensured structural consistency and content depth
6. **Validation**: Comprehensive testing of format, content, and language distribution

## License

This dataset is created for educational and research purposes, focusing on preserving and promoting Indramayu's cultural heritage through modern AI technology.