from typing import Dict, Tuple, List


def load_vocab(path: str) -> Dict[str, int]:
    """Load vocab and build word dict.
    Args:
        path: vocab path.
    """
    word_to_ix = {'[PAD]': 0, '[UNK]': 1}
    with open(path, 'r', encoding='utf-8') as f:
        for word in f.readlines():
            word = word.rstrip("\n")
            if word not in word_to_ix:
                word_to_ix[word] = len(word_to_ix)
    return word_to_ix


def load_dataset(seq_path: str, tag_path: str) -> Tuple[List[str], List[str]]:
    """Load dataset.
    """
    seqs = []
    tags = []
    with open(seq_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            seqs.append(line.split())
    with open(tag_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            tags.append(line.split())
    return seqs, tags
