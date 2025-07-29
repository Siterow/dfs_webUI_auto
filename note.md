# 如何自己写XPath定位？
先用开发者工具选中目标元素。
看它有没有唯一的属性（如id、name、data-xxx、class等）。
没有就用text()或contains(text(), 'xxx')。
组合父级元素特征可以让定位更稳。


html                                      XPATH
<span data-v-41f25160="">业务流程</span>  '//span[text()="业务流程"]'
<span class="txt txt-oneline">TEST-1130021|1地点车间1</span>  '//span[@class="txt txt-oneline" and text()="TEST-1130021|1地点车间1"]'
<div data-v-198aa673="" title="站点切换" element-loading-spinner="el-icon-loading" element-loading-background="rgba(0, 0, 0, 0.3)" class="link-item"><div data-v-198aa673="" class="el-image small sy-image"><img src="/obs/sys-resource/20220424/65304b238a214f7ead5b0e61f46ba6cd.png" class="el-image__inner"><!----></div><span data-v-198aa673="">站点切换</span></div>
"//div[contains(@class, 'link-item')]//span[text()='站点切换']"