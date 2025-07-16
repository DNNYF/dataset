#!/usr/bin/env python3
"""
Sample Output Display
Shows examples of the generated conversational data
"""

import json

def display_samples():
    """Display sample conversations from the dataset"""
    
    with open('dataset.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("=" * 80)
    print("SAMPLE CONVERSATIONS FROM INDRAMAYU TOURISM DATASET")
    print("=" * 80)
    
    # Show a few examples of Indonesian and Indramayu conversations
    samples = [0, 1, 2, 3]  # First 4 conversations
    
    for i, idx in enumerate(samples):
        conv = data[idx]
        question = conv['conversations'][0]['content']
        answer = conv['conversations'][1]['content']
        
        # Determine language
        if 'iku' in answer.lower() or 'nang' in answer.lower():
            lang = "Bahasa Indramayu"
        else:
            lang = "Bahasa Indonesia"
        
        print(f"\n{'='*5} SAMPLE {i+1} ({lang}) {'='*5}")
        print(f"❓ QUESTION: {question}")
        print(f"\n💬 ANSWER:")
        
        # Display answer with paragraph breaks
        paragraphs = answer.split('\n\n')
        for j, para in enumerate(paragraphs):
            print(f"\n📍 Paragraph {j+1}:")
            print(para)
        
        print(f"\n📊 Stats: {len(answer)} characters, {len(paragraphs)} paragraphs")
        print("-" * 80)

if __name__ == "__main__":
    display_samples()