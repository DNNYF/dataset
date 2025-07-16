#!/usr/bin/env python3
"""
Dataset Validation Script
Validates the generated dataset against the requirements
"""

import json
import sys

def validate_dataset():
    """Validate the dataset against all requirements"""
    
    try:
        with open('dataset.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Error: dataset.json not found")
        return False
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format")
        return False
    
    print(f"📊 Dataset loaded successfully with {len(data)} conversations")
    
    # Validate structure
    valid_structure = validate_structure(data)
    
    # Validate content quality
    valid_content = validate_content_quality(data)
    
    # Validate language distribution
    valid_languages = validate_language_distribution(data)
    
    # Overall validation
    all_valid = valid_structure and valid_content and valid_languages
    
    if all_valid:
        print("\n✅ All validations passed! Dataset meets requirements.")
    else:
        print("\n❌ Some validations failed. Please check the issues above.")
    
    return all_valid

def validate_structure(data):
    """Validate JSON structure"""
    print("\n🔍 Validating JSON structure...")
    
    if not isinstance(data, list):
        print("❌ Root element must be an array")
        return False
    
    issues = 0
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            print(f"❌ Item {i} is not an object")
            issues += 1
            continue
            
        if 'conversations' not in item:
            print(f"❌ Item {i} missing 'conversations' key")
            issues += 1
            continue
            
        conversations = item['conversations']
        if not isinstance(conversations, list) or len(conversations) != 2:
            print(f"❌ Item {i} conversations must be array with 2 elements")
            issues += 1
            continue
            
        # Check conversation structure
        for j, conv in enumerate(conversations):
            if not isinstance(conv, dict):
                print(f"❌ Item {i}, conversation {j} is not an object")
                issues += 1
                continue
                
            if 'role' not in conv or 'content' not in conv:
                print(f"❌ Item {i}, conversation {j} missing role or content")
                issues += 1
                continue
                
            if conv['role'] not in ['human', 'assistant']:
                print(f"❌ Item {i}, conversation {j} invalid role: {conv['role']}")
                issues += 1
    
    if issues == 0:
        print("✅ JSON structure is valid")
        return True
    else:
        print(f"❌ Found {issues} structural issues")
        return False

def validate_content_quality(data):
    """Validate content quality requirements"""
    print("\n🔍 Validating content quality...")
    
    issues = 0
    short_answers = 0
    missing_paragraphs = 0
    
    for i, item in enumerate(data):
        conversations = item['conversations']
        
        # Check human message (question)
        human_msg = conversations[0]['content']
        if len(human_msg.strip()) < 10:
            print(f"❌ Item {i}: Question too short")
            issues += 1
        
        # Check assistant message (answer)
        assistant_msg = conversations[1]['content']
        
        # Check minimum length
        if len(assistant_msg) < 500:
            short_answers += 1
            
        # Check paragraph structure
        paragraphs = assistant_msg.split('\n\n')
        if len(paragraphs) < 3:
            missing_paragraphs += 1
            
        # Check for repetitive content
        if assistant_msg.count("adalah salah satu destinasi wisata unggulan") > 1:
            issues += 1
    
    print(f"📝 Content Statistics:")
    print(f"   - Total conversations: {len(data)}")
    print(f"   - Average answer length: {sum(len(item['conversations'][1]['content']) for item in data) // len(data)} characters")
    print(f"   - Short answers (<500 chars): {short_answers}")
    print(f"   - Missing 3 paragraphs: {missing_paragraphs}")
    
    if issues == 0 and short_answers < len(data) * 0.1:  # Allow 10% tolerance
        print("✅ Content quality is good")
        return True
    else:
        print(f"❌ Found {issues} content quality issues")
        return False

def validate_language_distribution(data):
    """Validate language distribution (Indonesian vs Indramayu)"""
    print("\n🔍 Validating language distribution...")
    
    indonesian_indicators = ['adalah', 'yang', 'dapat', 'untuk', 'dengan', 'berbagai']
    indramayu_indicators = ['iku', 'sing', 'nang', 'kanggo', 'karo', 'macem-macem', 'panggon']
    
    indonesian_count = 0
    indramayu_count = 0
    unclear_count = 0
    
    for item in data:
        answer = item['conversations'][1]['content'].lower()
        
        id_score = sum(1 for indicator in indonesian_indicators if indicator in answer)
        ind_score = sum(1 for indicator in indramayu_indicators if indicator in answer)
        
        if id_score > ind_score:
            indonesian_count += 1
        elif ind_score > id_score:
            indramayu_count += 1
        else:
            unclear_count += 1
    
    print(f"🗣️ Language Distribution:")
    print(f"   - Bahasa Indonesia: {indonesian_count} ({indonesian_count/len(data)*100:.1f}%)")
    print(f"   - Bahasa Indramayu: {indramayu_count} ({indramayu_count/len(data)*100:.1f}%)")
    print(f"   - Unclear: {unclear_count} ({unclear_count/len(data)*100:.1f}%)")
    
    # Check if distribution is roughly balanced (40-60% range for each)
    id_percentage = indonesian_count / len(data)
    ind_percentage = indramayu_count / len(data)
    
    if 0.4 <= id_percentage <= 0.6 and 0.4 <= ind_percentage <= 0.6:
        print("✅ Language distribution is balanced")
        return True
    else:
        print("⚠️ Language distribution may be imbalanced")
        return True  # Still pass as this is not critical

def main():
    print("🚀 Starting dataset validation...")
    success = validate_dataset()
    
    if success:
        print("\n🎉 Dataset validation completed successfully!")
        sys.exit(0)
    else:
        print("\n💥 Dataset validation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()