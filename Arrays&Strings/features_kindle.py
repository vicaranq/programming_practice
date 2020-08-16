import os
import sys
import string

def get_top_k_features(requests, features, k):
    
    # If no input provided, return empty array
    if not features or not requests:
        return []

    # Create dictionary out of features
    features = {f:0 for f in features}
   
    # Loop over all requests
    for req in requests:
        # First, strip away any excess punctuation and split by space
        # Second, create a set of those words as we don't want duplicate counts
        for word in set(req.translate(str.maketrans('', '', string.punctuation)).split()):
            if word in features:
                # Increment word counter
                features[word]+=1

    # Sort result with max first
    result = [feat for feat, ct in sorted(features.items(), key=lambda x: x[1], reverse=True)]
    print(sorted(features.items(), key=lambda x: x[1], reverse=True))
    
    # Return top k results
    return result[:k]

def main():
    possible_features = [ 'waterproof', 'storage', 'durable', 'elastic', 'variety', 'updates' ]
    all_requests = [
                    'I wish it was more waterproof!',
                    'More storage!',
                    'needs more variety for me personally.',
                    'Updates update updates!!!!!',
                    'never hurts to be more elastic',
                    'decently durable tbh',
                    'needs to be waterproof',
                    'waterproof needed',
                    'more variety required for entertainment'
                   ]

    top_k = 2

    feats = get_top_k_features(all_requests, possible_features, top_k)
    print(feats)

if __name__ == "__main__":
    main()
