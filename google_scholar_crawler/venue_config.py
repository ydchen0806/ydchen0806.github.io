#!/usr/bin/env python3
"""
会议/期刊等级配置
用于筛选符合条件的一作论文（CCF B及以上 或 SCI 二区及以上）
"""

# CCF 等级配置
CCF_VENUES = {
    # CCF A 会议
    "AAAI": "A",
    "NeurIPS": "A",
    "NIPS": "A",
    "ICML": "A",
    "ICLR": "A",
    "CVPR": "A",
    "ICCV": "A",
    "ECCV": "A",
    "ACL": "A",
    "EMNLP": "A",
    "NAACL": "A",
    "IJCAI": "A",
    "SIGIR": "A",
    "KDD": "A",
    "WWW": "A",
    "ICDE": "A",
    "SIGMOD": "A",
    "VLDB": "A",
    "MICCAI": "B",  # CCF B
    
    # CCF B 会议
    "COLING": "B",
    "EACL": "B",
    "WACV": "B",
    "BMVC": "B",
    "ACCV": "B",
    "CIKM": "B",
    "ICASSP": "B",
    "INTERSPEECH": "B",
    "ICRA": "B",
    "IROS": "B",
    "ACM MM": "B",
    "MM": "B",
}

# SCI 期刊分区配置（中科院分区）
SCI_JOURNALS = {
    # Q1 顶刊
    "Nature": "Q1",
    "Science": "Q1",
    "Cell": "Q1",
    "TPAMI": "Q1",  # IEEE TPAMI
    "IEEE Transactions on Pattern Analysis and Machine Intelligence": "Q1",
    "IJCV": "Q1",  # International Journal of Computer Vision
    "International Journal of Computer Vision": "Q1",
    "TIP": "Q1",  # IEEE TIP
    "IEEE Transactions on Image Processing": "Q1",
    "TMI": "Q1",  # IEEE TMI
    "IEEE Transactions on Medical Imaging": "Q1",
    "JMLR": "Q1",  # Journal of Machine Learning Research
    "Medical Image Analysis": "Q1",
    "Nature Medicine": "Q1",
    "Nature Methods": "Q1",
    "Nature Communications": "Q1",
    "IEEE TNNLS": "Q1",
    "IEEE Transactions on Neural Networks and Learning Systems": "Q1",
    "TCSVT": "Q1",  # IEEE TCSVT
    "IEEE Transactions on Circuits and Systems for Video Technology": "Q1",
    
    # Q2 期刊
    "JBHI": "Q2",  # IEEE JBHI
    "IEEE Journal of Biomedical and Health Informatics": "Q2",
    "Neurocomputing": "Q2",
    "Pattern Recognition": "Q2",
    "Neural Networks": "Q2",
    "Knowledge-Based Systems": "Q2",
    "Expert Systems with Applications": "Q2",
    "Information Sciences": "Q2",
    "Applied Soft Computing": "Q2",
    "IEEE Access": "Q2",
    "Computers in Biology and Medicine": "Q2",
    "Artificial Intelligence in Medicine": "Q2",
}

def get_venue_level(venue_name: str) -> tuple:
    """
    获取会议/期刊的等级
    返回: (类型, 等级) 如 ('CCF', 'A') 或 ('SCI', 'Q1') 或 (None, None)
    """
    venue_upper = venue_name.upper()
    
    # 检查 CCF 会议
    for venue, level in CCF_VENUES.items():
        if venue.upper() in venue_upper:
            return ('CCF', level)
    
    # 检查 SCI 期刊
    for journal, level in SCI_JOURNALS.items():
        if journal.upper() in venue_upper:
            return ('SCI', level)
    
    return (None, None)


def is_qualified_venue(venue_name: str) -> bool:
    """
    判断是否为符合条件的会议/期刊
    条件：CCF B及以上 或 SCI 二区及以上
    """
    venue_type, level = get_venue_level(venue_name)
    
    if venue_type == 'CCF':
        return level in ['A', 'B']
    elif venue_type == 'SCI':
        return level in ['Q1', 'Q2']
    
    return False

