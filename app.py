import matplotlib.pyplot as plt
import pandas as pd
import os, itertools,re
from sklearn.cluster import KMeans
from flask import send_from_directory
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.getcwd()+r'\uploads'
RESULT_FOLDER = os.getcwd()+r'\result'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
up_f_name=''

@app.route('/up/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/result/<filename>')
def result_file_drop(filename):
    return send_from_directory(app.config['RESULT_FOLDER'],
                               filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('way'))
    data = open(os.getcwd()+r'\html\upload.html').read()    
    return data
@app.route('/way')
def way():
	statistic_create()
	data = open(os.getcwd()+r'\html\way.html').read()    
	return data
@app.route('/ret')
def ret():
	data = open(os.getcwd()+r'\html\ret.html').read()    
	return data


def statistic_create():
	f_n=''
	lst_for_stat=os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
	for i in lst_for_stat:
		if i.split('.')[-1]=='csv':
			f_n=i
			break
	print(os.getcwd()+r'\uploads\\'+f_n)
	seeds_df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], f_n))
	seeds_df.pop('person')


	def combine_list(stuff):
		return list(itertools.combinations(stuff,2))
	def k_mean(seeds_df,f_name):
		samples = seeds_df.values
		X=samples
		kmeans = KMeans(n_clusters=3)
		kmeans.fit(X)
		y_kmeans = kmeans.predict(X)
		plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=20, cmap='viridis')
		centers = kmeans.cluster_centers_
		plt.scatter(centers[:, 0], centers[:, 1], c='black', s=100, alpha=0.5);
		plt.savefig(f_name)
		plt.close()
		return 1

	stuff=['salary','lost','age','experience']
	comb_lst=combine_list(stuff)
	for i in comb_lst:
		res_df=seeds_df[list(i)]
		f_name=os.getcwd()+r'\result\{}.png'.format(i[0]+'-'+i[1])
		plt_res=k_mean(res_df,f_name)
	
	k_mean(seeds_df,os.getcwd()+r'\result\{}.png'.format('all'))

if __name__ == '__main__':
    app.run()