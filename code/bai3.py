import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

data  = load_data('C:/Users/84976/Desktop/BTL_PTIT/PYTHON/btl/results.csv')
# Lọc ra các cột có kiểu dữ liệu số
numeric_data = data.select_dtypes(include='number')

# Xử lý các giá trị NaN bằng cách thay thế bằng giá trị trung bình
imputer = SimpleImputer(strategy='mean')
numeric_data = imputer.fit_transform(numeric_data)

# Chuẩn hóa dữ liệu trước khi phân cụm
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Tìm số cụm tối ưu bằng phương pháp Elbow
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

# Vẽ biểu đồ Elbow
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Áp dụng KMeans với số cụm tối ưu, bạn chọn k từ phương pháp Elbow
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
data['Cluster'] = kmeans.fit_predict(scaled_data)

# Giảm chiều dữ liệu xuống 2D để trực quan hóa
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

# Vẽ biểu đồ phân cụm trên mặt phẳng 2D
# plt.figure(figsize=(8, 6))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=data['Cluster'], cmap='viridis')
plt.title('K-means Clustering with PCA')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()
