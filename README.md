@ -0,0 +1,39 @@
# Langchain Türkçe RAG Uygulaması

Bu proje, LangChain ve diğer kütüphaneleri kullanarak belge tabanlı bir soru-cevap sistemi oluşturur. PostgreSQL veritabanına bağlantı sağlar ve Google Generative AI ile embeddings kullanır.

## Başlangıç

Proje, Python ile yazılmıştır ve belirli kütüphaneleri gerektirir. Bu adımları izleyerek projeyi başlatabilirsiniz.

### Gereksinimler

Bu projede aşağıdaki kütüphaneler kullanılmaktadır:

- `langchain`
- `langchain_community`
- `langchain_google_genai`
- `psycopg2-binary`
- `python-dotenv`
- `langchain-openai`
- `pdfminer.six`

Bu kütüphaneleri yüklemek için, aşağıdaki komutu kullanarak `requirements.txt` dosyasını kullanabilirsiniz:

```bash
pip install -r requirements.txt

Kurulum
git clone <proje-repo-url>
cd <proje-dizini>


Sanal Ortam Oluşturma ve Aktifleştirme (Opsiyonel, önerilir):
python -m venv venv
source venv/bin/activate  # Unix/macOS
.\venv\Scripts\activate   # Windows

Gereksinimleri Yükleme:
pip install -r requirements.txt
---------------------------------
 // Proje Örnek Soru Cevapları //
“Ulusal Yapay Zekâ Stratejisi
 ++ Yönlendirme Kurulu” hakkında bilgi verir misin?


-- Ulusal Yapay Zekâ Stratejisi Yönlendirme Kurulu Hakkında Bilgi
Amaç: Ulusal Yapay Zekâ Stratejisi (UYZS) kapsamında belirlenen stratejik önceliklere ulaşmak için, stratejik düzeyde koordinasyonu sağlamak ve yapay zekâ projelerinin izlenmesini ve yönetilmesini sağlamak amacıyla kurulmuştur​(TR-UlusalYZStratejisi20…).

Görevler:

Eylem Planlarının Hazırlanması: UYZS’de belirlenen tedbirlere ilişkin detaylı eylem planlarını hazırlamak ve uygulanmasını koordine etmekten sorumlu bakanlıkları belirlemek.
Üst Düzey Koordinasyon: Eylem planlarının birbirleriyle uyumlu şekilde hazırlanması için üst seviye koordinasyonu sağlamak ve UYZS ile bu eylem planlarının uygulanmasını üst seviyede izlemek.
Kurumlar Arası Eş Güdüm: Kurumlar arası eş güdümü temin ederek, YZ stratejilerinin etkili bir şekilde hayata geçirilmesini sağlamak​(TR-UlusalYZStratejisi20…).



-----------------------


 ++ Tubitak' ın yapay zeka ar-ge lerine ayırdığı bütçeleri listeler misin?

--TÜBİTAK’ın yapay zekâ alanında ayırdığı AR-GE bütçeleri ve destekleri şu şekildedir:
Sanayinin Dijital Dönüşümü ve İleri İmalat Sistemleri: 282.658.608 TL, toplam bütçenin %18'i
Ticarette Dijital Dönüşüm: 152.629.419 TL, toplam bütçenin %10'u
Akıllı Yaşam ve Sağlık: 139.408.178 TL, toplam bütçenin %9'u
Oyun, Medya ve Eğlence: 133.749.626 TL, toplam bütçenin %9'u
Finans Sektöründe Dijital Dönüşüm: 127.778.712 TL, toplam bütçenin %8'i
Savunma ve Güvenlik: 116.823.161 TL, toplam bütçenin %7'si
Mobilite Sektörleri: 82.142.583 TL, toplam bütçenin %5'i
Enerji ve Yeraltı Kaynakları: 67.625.237 TL, toplam bütçenin %4'ü
Eğitimde Dijital Dönüşüm: 52.426.164 TL, toplam bütçenin %3'ü
5G ve Ötesi Teknolojiler ile Bağlantılı Yaşam: 46.966.846 TL, toplam bütçenin %3'ü
Gıda, Tarım ve Hayvancılık Sektörü: 44.992.474 TL, toplam bütçenin %3'ü
Sosyal Bilimler (Hukuk dahil): 28.029.761 TL, toplam bütçenin %2'si
Doğal Afetlerin Önlenmesi ve Kriz Yönetiminde Dijital Dönüşüm: 11.945.636 TL, toplam bütçenin %1'i
Diğer: 9.385.191 TL, toplam bütçenin %1'i
Toplam: 1.566.647.146


--------------------------

++ CBDDO tarafından, kamu kurumlarında YZ ve ileri analitik çalışmaları hakkında bilgi verir misin? 

-- CBDDO (Cumhurbaşkanlığı Dijital Dönüşüm Ofisi), kamu kurumlarında YZ (Yapay Zekâ) ve ileri analitik çalışmalarını hızlandırmak için Kamu YZ Ekosistemi'nin oluşturulması ve yönetilmesinde önemli bir rol oynar. Bu ekosistem, merkezi ve yerel yönetim kurum ve kuruluşlarının YZ ve ileri analitik projelerinin takibi, rehberler doğrultusunda desteklenmesi ve koordinasyonun sağlanmasını içerir​(TR-UlusalYZStratejisi20…).

Kamu YZ Ekosistemi'nin Özellikleri ve Görevleri
Proje Koordinasyonu:

Bakanlıklar başta olmak üzere, merkezi ve yerel yönetim kurumlarının YZ ve ileri analitik projelerinin koordinasyonunu sağlar.
Projelerin planlanması, geliştirilmesi ve işletilmesi süreçlerini organize eder​(TR-UlusalYZStratejisi20…).
Envanter Oluşturma ve Stratejik İhtiyaçların Karşılanması:

Merkezî ve yerel yönetimlerde YZ ve ileri analitik projeleri ile alan uzmanları için envanter oluşturur.
Kurum ve kuruluşlarda gerçekleştirilen organizasyonel yapılanma ve alan uzmanı istihdamı için ihtiyaçların karşılanması amacıyla gerekli koordinasyonu sağlar​
