---
domain: 人工智能与前沿技术
type: MOC
status: 整理中
created: 2026-07-29
course: 人工智能技术
chapter: 7
section: 0
tags: ["人工智能","机器学习","深度学习","CV","NLP","大模型","AI竞赛","考研408"]
prerequisites: ["第6章-深度学习基础神经网络"]
source: 《人工智能导论》本科通用教材、人工智能考研讲义
---

# 第7章 计算机视觉核心算法 — 目录总览 (MOC)

> [!info] 章节概览
> 本章系统介绍计算机视觉（Computer Vision, CV）的核心算法体系。从最基础的图像分类任务出发，逐步深入到目标检测（定位+分类）和图像分割（像素级理解），并覆盖经典网络架构、检测算法家族、分割方法演进以及特征匹配等关键技术。

## 🗺️ 学习路线图

```mermaid
flowchart LR
    A["👁️ 计算机视觉<br/>从图像到理解"] --> B["📚 7.1 图像分类与经典网络"]
    B --> C["🎯 目标检测<br/>定位 + 分类"]
    C --> D["📚 7.2 目标检测算法"]
    D --> E["✂️ 图像分割<br/>像素级理解"]
    E --> F["📚 7.3 图像分割与特征提取"]

    style A fill:#4a90d9,stroke:#333,color:#fff
    style B fill:#e8f4fd,stroke:#4a90d9
    style C fill:#f5a623,stroke:#333,color:#fff
    style D fill:#fff8e1,stroke:#f5a623
    style E fill:#52c41a,stroke:#333,color:#fff
    style F fill:#e8f5e9,stroke:#52c41a
```

## 📖 章节内容

### 7.1 图像分类与经典网络
- [[7.1-图像分类与经典网络]]
- 图像分类任务定义与评价指标
- 经典 CNN 架构进阶：VGGNet、GoogLeNet、ResNet、DenseNet
- Vision Transformer (ViT) 架构解析
- 迁移学习与预训练模型使用
- PyTorch 图像分类实战

### 7.2 目标检测算法
- [[7.2-目标检测算法]]
- 目标检测任务定义与评价指标（mAP、IoU）
- Two-Stage 检测算法：R-CNN、Fast R-CNN、Faster R-CNN
- One-Stage 检测算法：YOLO 系列、SSD
- Anchor-Free 检测算法：CenterNet、FCOS
- NMS 非极大值抑制
- PyTorch 目标检测实战

### 7.3 图像分割与特征提取
- [[7.3-图像分割与特征提取]]
- 分割任务类型：语义分割、实例分割、全景分割
- 语义分割：FCN、U-Net、DeepLab 系列
- 实例分割：Mask R-CNN
- 特征提取与匹配：SIFT、SURF、特征点匹配
- PyTorch 图像分割实战

## 🎯 核心考点

| 考点 | 重要程度 | 常考形式 |
|------|---------|---------|
| 图像分类评价指标（Top-1/Top-5 准确率） | ⭐⭐⭐ | 简答题 |
| VGGNet 统一 3×3 卷积核设计思想 | ⭐⭐⭐⭐ | 简答题 |
| ResNet 残差连接原理与作用 | ⭐⭐⭐⭐⭐ | 简答题、证明题 |
| ViT 架构与 CNN 的区别 | ⭐⭐⭐⭐ | 简答题、分析题 |
| R-CNN 家族对比（R-CNN/Fast/Faster） | ⭐⭐⭐⭐⭐ | 简答题、对比题 |
| YOLO 系列演进与核心思想 | ⭐⭐⭐⭐⭐ | 简答题 |
| Anchor-Based vs Anchor-Free 检测 | ⭐⭐⭐⭐ | 分析题 |
| NMS 非极大值抑制算法 | ⭐⭐⭐⭐ | 简答题、计算题 |
| 语义分割 vs 实例分割 vs 全景分割 | ⭐⭐⭐⭐ | 简答题 |
| FCN 全卷积网络思想 | ⭐⭐⭐⭐⭐ | 简答题 |
| U-Net 编码器-解码器结构 | ⭐⭐⭐⭐ | 简答题 |
| IoU/PA 分割评价指标计算 | ⭐⭐⭐⭐ | 计算题 |

## 📝 自测题

1. **计算题**：在图像分类任务中，假设一个 10 类分类器的预测结果为 $[0.1, 0.3, 0.05, 0.2, 0.15, 0.02, 0.08, 0.05, 0.03, 0.02]$，真实标签为类别 1（索引从 0 开始）。计算 Top-1 和 Top-5 准确率是否正确。

2. **简答题**：对比 R-CNN、Fast R-CNN 和 Faster R-CNN 三者的核心改进点，并说明为什么 Faster R-CNN 是 Two-Stage 检测的代表性算法。

3. **计算题**：给定一个目标检测场景，预测了 5 个边界框（BBox），与真实框的 IoU 分别为 $[0.9, 0.8, 0.75, 0.6, 0.3]$。设 IoU 阈值为 0.5，计算每个预测是 TP（True Positive）还是 FP（False Positive）。

4. **应用题**：某自动驾驶系统需要实时检测车辆和行人。要求检测速度快（>30 FPS）且精度高。请选择合适的检测算法，并说明理由。

5. **分析题**：从架构设计角度对比 CNN 和 ViT 在图像分类任务上的主要差异，分析 ViT 为什么能在大数据集上超越 CNN。

6. **计算题**：给定语义分割的混淆矩阵，计算 Pixel Accuracy、Mean IoU 和 Dice Coefficient。混淆矩阵（4 类）：
   $$
   \begin{bmatrix}
   80 & 5 & 3 & 2 \\
   6 & 70 & 8 & 4 \\
   4 & 10 & 65 & 1 \\
   2 & 3 & 5 & 85
   \end{bmatrix}
   $$

## 🔗 关联知识点

- [[第6章-深度学习基础神经网络#6.2-卷积神经网络CNN]] → CNN 基础架构、ResNet 残差连接
- [[第6章-深度学习基础神经网络#6.3-优化算法与正则化]] → Adam、学习率调度、正则化
- [[第7章-计算机视觉核心算法#7.1-图像分类与经典网络]] → VGGNet/ResNet/ViT 详解
- [[第7章-计算机视觉核心算法#7.2-目标检测算法]] → R-CNN/YOLO/SSD 对比
- [[第7章-计算机视觉核心算法#7.3-图像分割与特征提取]] → FCN/U-Net/Mask R-CNN
- [[第8章-序列模型与Transformer]] → Transformer 架构、Self-Attention
- [[第10章-多模态大模型]] → CLIP、视觉-语言模型