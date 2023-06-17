
<strong>Usage</strong>

<p>To create a new project, run the script with the following command-line arguments:</p>

<pre>
<code>python dev.py -c &lt;category&gt; -t &lt;technology&gt; -np &lt;project_name&gt;</code>
</pre>

<p>&lt;category&gt;: Specify the category of the project. Choose from 'hrv', 'cev', 'pup', 'wk', or 'csj'.</p>
<p>&lt;technology&gt;: Specify the technology of the project. Choose from 'py', 'web', or 'js'.</p>
<p>&lt;project_name&gt;: Provide the name of the new project.</p>

<p>Example:</p>

<pre>
<code>python dev.py -c &lt;category&gt; -nt &lt;new_technology_name&gt; -np &lt;project_name&gt;</code>
</pre>

<p>&lt;category&gt;: Specify the category of the project. Choose from 'hrv', 'cev', 'pup', 'wk', or 'csj'.</p>
<p>&lt;technology&gt;: Specify the technology of the project. Name it with a techlogy that dosen't exist.</p>
<p>&lt;project_name&gt;: Provide the name of the new project.</p>

<p>To list existing projects within a specific category and technology, run the script with the following command-line arguments:</p>

<pre>
<code>python dev.py -c &lt;category&gt; -t &lt;technology&gt; -op</code>
</pre>

<p>Example:</p>

<pre>
<code>python dev.py -c pup -t py -op</code>
</pre>

<p><strong>Important Note:</strong> Please remember to modify the code according to your own directory structure before using it.</p>

<p>Feel free to customize and enhance the script according to your specific needs. Happy coding!</p>
