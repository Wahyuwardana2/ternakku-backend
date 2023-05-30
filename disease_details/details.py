def get_disease_details(predicted_class):
    if predicted_class == 'Cocciodiosis':
        disease_details = "Coccidiosis adalah penyakit parasit umum pada unggas yang disebabkan oleh protozoa dari genus Eimeria. Penyakit ini mempengaruhi saluran pencernaan dan dapat menyebabkan diare, penurunan berat badan, dan penurunan produksi telur."
        handling_method = "Untuk mengelola Coccidiosis, penting untuk menjaga kebersihan yang baik di tempat pemeliharaan unggas, menyediakan air minum yang bersih, dan menggunakan obat anticoccidial yang sesuai."
    elif predicted_class == 'Healthy Chickens':
        disease_details = "Ayam Anda terlihat sehat."
        handling_method = "Terus berikan nutrisi yang tepat, air bersih, dan jaga kebersihan yang baik untuk memastikan kesehatan mereka."
    elif predicted_class == 'Healthy Cows':
        disease_details = "Sapi Anda terlihat sehat."
        handling_method = "Terus berikan nutrisi yang tepat, air bersih, dan jaga kebersihan yang baik untuk memastikan kesehatan mereka."
    elif predicted_class == 'Lumpy Cows':
        disease_details = "Penyakit sapi berbintik, juga dikenal sebagai Penyakit Kulit Berbintik Bovine (LSD), adalah penyakit viral yang mempengaruhi sapi. Penyakit ini ditandai dengan demam, nodul kulit, dan pembengkakan."
        handling_method = "Untuk mengelola penyakit sapi berbintik, penting untuk mengisolasi hewan yang terinfeksi, menerapkan langkah pengendalian vektor, dan memberikan perawatan suportif. Konsultasikan dengan dokter hewan untuk opsi pengobatan yang spesifik."
    elif predicted_class == 'Salmonella':
        disease_details = "Salmonella adalah infeksi bakteri yang dapat mempengaruhi unggas maupun ternak. Penyakit ini dapat menyebabkan diare, dehidrasi, dan dalam kasus yang parah, kematian."
        handling_method = "Untuk mengelola infeksi Salmonella, penting untuk menjaga kebersihan yang baik, menyediakan air minum yang bersih, dan menerapkan langkah biosekuriti. Pemberian antibiotik yang sesuai mungkin diperlukan setelah berkonsultasi dengan dokter hewan."
    else:
        disease_details = "Penyakit tidak diketahui"
        handling_method = "Silakan konsultasikan dengan dokter hewan untuk diagnosis dan pengobatan lebih lanjut."

    return disease_details, handling_method

