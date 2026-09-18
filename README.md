# Лаборатори №2 — k6 гүйцэтгэлийн хэмжүүр

**Оюутан:** Х.Цогтбаяр  
**Оюутны код:** B232270072

## Зорилго

Энэ лабораторийн ажлаар Grafana k6 ашиглан веб серверийн гүйцэтгэлийг
өөр өөр ачааллын түвшинд хэмжиж, latency, throughput болон error rate-ийг
харьцуулна.

## k6 version

```text
k6 v2.2.0 (commit/00a9a1b7f5, go1.26.5, linux/amd64)
```

## Гурван түвшний харьцуулсан хүснэгт

| VU | p90 | p95 | Throughput (req/s) | Error rate | Threshold |
|---:|---:|---:|---:|---:|:---|
| 5 | 101.67 ms | 101.87 ms | 4.503169 | 0.00% | ✓ PASS |
| 30 | 906.18 ms | 1.1 s | 9.427226 | 0.00% | ✗ FAIL (зөвхөн duration) |
| 100 | 56.94 s | 56.94 s | 3.522199 | 33.75% | ✗ FAIL (duration + error) |

Дэлгэрэнгүй screenshot болон бүтэн текст гаралт:
- `screenshots/k6-summary-05vu.png`, `results/run-05vu.txt`
- `screenshots/k6-summary-30vu.png`, `results/run-30vu.txt`
- `screenshots/k6-summary-100vu.png`, `results/run-100vu.txt`
- `results/baseline-05vu-30s.txt` — Алхам 2-ын 5 VU / 30 секундийн baseline
- `results/run-pass-30vu.txt` — 30 VU / 1 минутын SLO PASS (`p95 < 153 ms`)
- `results/run-fail.txt` — зориуд хатуу `p95 < 100 ms` SLO FAIL
- `results/run-stages.txt` — 5 → 30 → 100 → 0 VU stages-ийн бүтэн output

## SLO ба тайлбар

Алхам 2-ын 5 VU / 30 секундийн baseline-ийн p95 = 101.87 ms гарсан. SLO-г baseline p95 × 1.5 гэж тооцож, 101.87 × 1.5 = 152.805 ms буюу p95 < 153 ms гэж сонгосон. Мөн error rate < 1% гэж тогтоосон. 30 VU / 1 минутын PASS output нь энэ SLO-г шалгана, харин `script-fail.js`-ийн p95 < 100 ms нь зориуд FAIL гаргана. Baseline-ийн бүтэн output нь `results/baseline-05vu-30s.txt` файлд хадгалагдсан.

Stages туршилтыг [script-stages.js](script-stages.js)-ээр 5 → 30 → 100 → 0 VU дарааллаар ажиллуулж, бүтэн summary-г [results/run-stages.txt](results/run-stages.txt)-д хадгалсан. Stages нь нэгтгэсэн summary өгдөг тул 5/30/100 VU-ийн хүснэгтийг тусдаа run-уудаас авсан.

## Дүгнэлт (8-10 өгүүлбэр)

5 VU-ийн baseline тестэд p95 = 101.87 ms, error rate 0% гарсан. ThreadingHTTPServer ашигласнаар 30 VU-ийн PASS тестэд олон хүсэлт зэрэг боловсруулагдаж, p95 нь 153 ms-ийн SLO дотор үлдэх боломжтой болсон. 100 VU-д throughput өсөх боловч системийн нөөц болон queue-ийн нөлөөгөөр p95 муудаж болно. Stages тест нь ачааллыг 5-оос 30, 100 VU хүртэл өсгөөд буцаан 0 болгосон ерөнхий явцыг харуулсан. Throughput нь VU өсөхөд эхлээд нэмэгдэж, системийн хязгаарт хүрвэл цааш нэмэгдэхгүй байж болно. p95 нь дундажаас илүү олон хэрэглэгчийн муу туршлагыг илрүүлдэг хэмжүүр юм. Error rate < 1% нь үйлчилгээний найдвартай байдлыг шалгасан. SLO-г дурын 300 эсвэл 520 ms тоогоор биш, baseline p95 = 101.87 ms-ийн 1.5 дахин үржвэрээр тооцож p95 < 153 ms болгосон. 30 VU PASS болон p95 < 100 ms зориудын FAIL output-ууд тусдаа файлд хадгалагдсан. Иймээс энэ лаборатори latency, throughput, error rate, availability хэмжүүрүүдийг бодит k6 output-оор харуулсан.