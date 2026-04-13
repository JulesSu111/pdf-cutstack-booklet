# PDF Booklet App
- 用于将A4 PDF 快速缩印为4开大小的小册子
- Quickly convert A4 PDFs into compact quarter-size booklets.
- A4-PDFs in Sekundenschnelle zu kompakten Viertelheften umwandeln.

Like it? Give it a **star**.  
Bug? Open an **issue**.  
Got a feature wish? Tell me.

# A4 PDF Cut-Stack Booklet

Language: [ZHN](#zhn) / [ENG](#eng) / [DEU](#deu)

<a id="zhn"></a>
# 中文
用于将A4 PDF 快速缩印为小册子
你好，我想要**star**，谢谢你！
欢迎 **issue**。  
欢迎 **意见与建议**

#特性：
- 适用于任意 A4 大小 PDF
- 使用A4 纸双面打印一张纸可排 8 页
- 无需手动排版
- 成册流程仅需三步：切开 → 上下摞起 → 中间一折 → 搞定！
- 支持 竖版 PDF 与 横版 PDF

#当前功能
- 小册子页序自动排版
- 适配切开后直接整摞叠放的页序逻辑
- 竖版 PDF 支持
- 横版 PDF 支持
- 页边距设置
- 页面旋转设置
- 背面 180° 旋转
- 裁切辅助线

#使用流程
1. 选择输入 PDF  
2. 选择输出路径  
3. 生成输出 PDF  
之后按以下流程处理：
*打印 → 切开 → 上下摞起 → 中间一折*

#计划功能
- 裁剪方式示意图
- 书脊方向选择（上 / 下 / 左 / 右）
- 辅助线格式自定义
- 输出前预览排版顺序
- 添加页码

------------------------------------------------
<a id="eng"></a>
# English

For quickly turning A4 PDFs into booklets

#Features:
- Suitable for any A4-sized PDF
- Uses double-sided A4 printing, with up to 8 pages on one sheet
- No manual layout required
- The booklet workflow only needs three steps: cut → stack → fold in the middle → done!
- Supports both portrait PDFs and landscape PDFs

#Current Features
- Automatic booklet page ordering
- Page ordering logic designed for direct full-stack stacking after cutting
- Portrait PDF support
- Landscape PDF support
- Margin setting
- Page rotation setting
- 180° back-side rotation
- Cutting guide lines

#Workflow
1. Select input PDF  
2. Select output path  
3. Generate output PDF  
Then process it as follows:
*print → cut → stack → fold in the middle*

#Planned Features
- Cutting guide diagram
- Spine direction selection (up / down / left / right)
- Custom guide line styles
- Layout preview before export
- Add page numbers

------------------------------------------------
<a id="deu"></a>
# Deutsch
Zum schnellen Umwandeln von A4-PDFs in Broschüren

#Eigenschaften:
- Geeignet für beliebige PDFs im A4-Format
- Beidseitiger Druck auf A4, mit bis zu 8 Seiten auf einem Blatt
- Keine manuelle Seitenanordnung nötig
- Der Broschürenablauf braucht nur drei Schritte: schneiden → stapeln → in der Mitte falten → fertig!
- Unterstützung für Hochformat-PDFs und Querformat-PDFs

#Aktuelle Funktionen
- Automatische Broschüren-Seitenreihenfolge
- Seitenlogik für direktes Stapeln ganzer Stapel nach dem Schneiden
- Unterstützung für Hochformat-PDFs
- Unterstützung für Querformat-PDFs
- Randeinstellung
- Rotationseinstellung
- 180°-Drehung der Rückseite
- Schneidehilfslinien

#Verwendung
1. Eingabe-PDF auswählen  
2. Ausgabepfad auswählen  
3. Ausgabe-PDF erzeugen  
Danach wie folgt weiterverarbeiten:
*drucken → schneiden → stapeln → in der Mitte falten*

#Geplante Funktionen
- Schneide-Schaubild
- Auswahl der Rückenrichtung (oben / unten / links / rechts)
- Anpassbare Hilfslinien
- Vorschau der Seitenanordnung vor dem Export
- Seitenzahlen hinzufügen

Gefällt es dir? Gib einen **Star**.  
Bug gefunden? Bitte ein **Issue** erstellen.  
Feature-Wunsch? Einfach Bescheid geben.



# Dependencies / 依赖库 / Abhängigkeiten
- Python 3.x
- PySide6
- pypdf
