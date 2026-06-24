import json
import sys
import numpy as np
from sklearn.metrics import f1_score, accuracy_score


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def score(pred_file, ref_file):
    """纯净打分：输入预测文件 + 参考文件，输出宏平均F1"""
    pred_data = load_json(pred_file)
    ref_data = load_json(ref_file)

    pred_map = {item['id']: item['label'] for item in pred_data}

    y_true = []
    y_pred = []
    missing = 0
    for item in ref_data:
        tid = item['id']
        y_true.append(item['label'])
        if tid in pred_map:
            y_pred.append(pred_map[tid])
        else:
            y_pred.append(-1)
            missing += 1

    if missing > 0:
        print(f'⚠ 缺少 {missing} 个样本的预测，按错误处理')

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    mask = y_pred == -1
    y_pred = np.where(mask, (y_true + 1) % 3, y_pred)

    macro_f1 = f1_score(y_true, y_pred, average='macro')
    accuracy = accuracy_score(y_true, y_pred)
    class_f1 = f1_score(y_true, y_pred, average=None)

    print('=' * 50)
    print('评分结果')
    print('=' * 50)
    print(f'总样本数: {len(y_true)}')
    print(f'宏平均F1-Score: {macro_f1:.6f}')
    print(f'准确率: {accuracy:.6f}')
    print(f'各类别F1: HWT(0)={class_f1[0]:.6f}, LGT(1)={class_f1[1]:.6f}, HLT(2)={class_f1[2]:.6f}')

    return {
        'macro_f1': float(macro_f1),
        'accuracy': float(accuracy),
        'class_f1': [float(f) for f in class_f1]
    }


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('用法: python score.py <prediction.json> <reference.json>')
        sys.exit(1)

    result = score(sys.argv[1], sys.argv[2])
    out_file = 'scores.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f'\n已保存: {out_file}')