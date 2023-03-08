# Step Four: Add templates and translatable content

Now that we have your models set up and your database has been configured for the data you're planning to use in your blog, we can start focusing more on how things will look on the frontend and how people will interact with your multilingual website.

## Set up your home page

Navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in to the backend of the website. On the lefthand menu, click on "Pages", then click on "Home". On the "Home" page, find the three purple dots to open the action menu and click "Edit".

Now we're (finally) going to add some data to our blog. Feel free to choose your own theme. But if you're not feeling particularly inspired, you can join me in filling out "Badger Blog" for the title and "Musings on Earth's most noble and distinctive mammal" for the summary. You'll need a picture too. Feel free to use this [lovely badger](https://upload.wikimedia.org/wikipedia/commons/4/41/M%C3%A4yr%C3%A4_%C3%84ht%C3%A4ri_4.jpg) from Wikimedia Commons. Click "Choose an image" and then upload the image to Wagtail.

![Screenshot of home page in Wagtail admin](https://www.meagenvoss.com/media/images/Screen_Shot_2022-09-28_at_9.16.11_PM.original.png)

When you're done adding the content, go to the bottom of the page and use the big green button to save your draft. Then click on the arrow next to "Save draft" to open up the publish menu and click "Publish" to publish the page.

![Screenshot of Wagtail publish button](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-05_at_11.56.07_PM.original.png)


## Update the home page template

Now, if you were to navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) right now, you would still see the pretty swaying egg page. That's because we need to update the code so that it isn't using the default template that comes with Wagtail.

 can pull the content you just created into your templates.

Go to `home/templates/home/home_page.html` and delete everything in the file except for the first line `{% extends "base.html" %}`. Update the file so it looks like this:

```
{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

{% block body_class %}template-homepage{% endblock %}

{% block content %}

<h1>{{ page.title }}</h1>

<p>{{page.summary}}</p>

{% image page.main_image max-500x500 %}

{% endblock %}
```
Save the file and then reload your homepage. You should now see the title of your blog, the summary, and a beautiful badger (if you chose to go with my badger theme rather than your own).

Now, the summary might look a little funky. And that is because text fields do not print with escaped characters by default. Fortunately, Wagtail comes with a handy filter, among many other [handy filters](https://docs.wagtail.org/en/stable/topics/writing_templates.html#template-tags-and-filters), that can render the text properly. Update the `{{page.summary}}` line so that it is:

```
<p>{{page.summary|richtext}}</p>
```
Refresh the page and the summary text should be displaying properly now.

Before you move on from this task, let's clean your templates and organize things a bit. Navigate to `myblog\templates` and create a new directory in it called `home`. Move `home_page.html` to the new `home` directory. Refresh the page to make sure it still works. The delete the `templates` directory in the `home` app. While you're there, you can also delete the `static` folder in the the `home` app because all that is in it is some CSS for the default home page.

This structure will help you stay organized by keeping all of your templates in one directory. Trust me, any frontend developers you work with will thank you. And then they will find something else to pick on, but that's the way of things.



## Set up simple blog templates

Now that the home page is set up, let's set up some simple templates for your blog pages as well. First, let's create some content in the backend of Wagtail to work with. Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and click the "Pages" menu then click "Badger Blog" (or whatever title you chose) to open the menu for that page. Click the three purple dots to open the action menu and click "Add child page". Choose the "Blog index page" this time.

![Screen shot of action menu from home page](https://www.meagenvoss.com/media/images/Screen_Shot_2022-09-28_at_9.04.21_PM.original.png)

 Fill out the title and intro line for your blog. I used the oh-so-creative title "Blog" and "The latest badger sightings" if you would like to steal those brilliant lines. Use the big green button at the bottom to "Publish" the page.

Back in the "Badger Blog" section of Wagtail, you should now see a line for your "Blog" page. When you hover over "Blog", a button should appear that says "Add child page." Click the button. Pick "Blog page".

![Screenshot of the Blog page in the list](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-03_at_3.47.11_PM.original.png)

Fill out some content on your blog page. If your creative muse has deserted you to sip margharitas on a beach, then you can add today's date, use the title "Badgers are brilliant" and the intro line "We have totally underestimated badgers".

Now the body is where you get to play with StreamField for the first time. All you need to do is add one block of content to the body. You can add an image if you want or a text paragaph like:

```
Here are three reasons badgers are more intelligent than we thought they were:

    1. They use tools
    2. They can solve puzzles
    3. They can break out of zoos

```
After you add your content, use the big green button at the bottom of the page and click "Publish".

Now that you entered some content, let's create some templates to go with it. First, go to `myblog/templates` and create a directory labeled `blog`. In that `blog` directory, create two blank files: `blog_index_page.html` and `blog_page.html`

In `blog_index_page.html`, let's add:

```
{% extends "base.html" %}

{% load wagtailcore_tags %}

{% block body_class %}template-blogindexpage{% endblock %}

{% block content %}
    <h1>{{ page.title }}</h1>

    <div class="intro">{{ page.intro|richtext }}</div>

    {% for post in page.get_children %}
        <h2><a href="{% pageurl post %}">{{ post.title }}</a></h2>
        {{ post.specific.intro }}
        {{ post.specific.body }}
    {% endfor %}

{% endblock %}
```

Save that file and then add the following code to `blog_page.html`:

```
{% extends "base.html" %}

{% block body_class %}template-blogpage{% endblock %}

{% block content %}
    <h1>{{ page.title }}</h1>
    <p class="meta">{{ page.date }}</p>

    <div class="intro">{{ page.intro }}</div>

    {{ page.body }}

    <p><a href="{{ page.get_parent.url }}">Return to blog</a></p>

{% endblock %}
```

Excellent! Now you have some basic templates for your blog content in English that you can work with. Let's have a quick look at your content by checking that it works. In the Wagtail admin, navigate to "Pages" then click "Badger Blog". You should see your "Blog" page listed like this:

![Screenshot of Wagtail showing Badger Blog listing](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-12_at_10.19.28_PM.original.png)

Hover over the "Blog" listing to make the buttons appear then click "View live" to see what your `BlogIndex` page looks like. You should be able to click on your blog article and open up your "Badgers are brilliant" blog then navigate back to your "Blog" page. The "Home" page and the "Blog" page aren't connected yet. Don't worry, we'll get there.


First, let's work on translating some of this content so that we have some content in French to work with as well.

## Setting up your new locale

To set up a locale for French, go to the lefthand menu, click "Settings", then click "Locales". On the righthand side, click the green "Add a locale" button. In the "Language" dropdown menu, choose "French". 

Beneath the dropdown is an option to synchronize content from the main language of your website. Click the green "Enable" button. Check the "Enabled" checkbox and then select "English" from the "Sync from" menu. Click "Save" to save your changes.

![Screenshot showing how to add a locale to Wagtail](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-03_at_4.21.46_PM.original.png)

Now click "Pages" on the lefthand menu and you'll see there are now _two_ versions of "Badger Blog." One says "English" next to it and the other says "French." You might also find two copies of the "Welcome to Wagtail!" page. Feel free to delete those or ignore them. They are not important anymore. 


Click on the "French" version of "Badger Blog" to edit it. You'll be presented with an option to translate the "Badger Blog" page and all of the pages in the subtree. Check the box to translate all of the pages. 

![Screenshot showing the translate subtree option in Wagtail](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-03_at_4.23.52_PM.original.png)

Now when you open the "Pages" menu, you should see two copies of your page trees: one labeled "English" and another labeled "French".

Click "Edit" for the French version of the "Badger Blog" Page to edit the content. The page will open up in a translation view. The translation view provides the content in the original language and provides you with some different options to translate it.

![Screenshot of the initial translation view for Badger Blog](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-13_at_6.58.01_AM.original.png)

## Translate using PO files

PO files are the file format used by professional translators for translating a variety of structured content, including websites. If you are going to be working with a living, breathing human translator, this could be a good option for your project. The advantages of the PO file is that everything can be translated in one file, and you can send that file to a translator without having to give them access to the admin section of your website.

To use the PO file method, click the "Download PO file" button to download the file. Then either send the file to a translator or use a program like [Poedit](https://poedit.net/download) to edit the file and translate it. Once the file has been translated, you can upload it to your page with the "Upload PO File" button.

Once the file is uploaded, check that there are green checkmarks throughout your page. Click the promote tab too and make sure the slug has been translated as well. Once everything is translated click the big green "Publish in French" button at the bottom to publish the page.

## Translate manually

You can also use the Wagtail Localize plugin to translate content manually as well. This approach is best to use if you decide you are okay with creating a log in for your translator or if someone who will be working on the website regularly is also translating the content. To do manually translation, go through each item on the page and click "Translate". Once you are done adding the translation, click "Save" to save your changes. Do this for each piece of content on the page. Click the "Promote" tab to translate the slug as well. Once you're done, click "Publish in French" at the bottom of the page to publish the page.

**NOTE** Be very careful of using quote marks in your translations. Quote marks in certain languages are different from the quote marks used in HTML. So if there are any links in your content, you need to make sure you're using the right type of quote marks in any HTML included in your translations.

## Machine translation

You can also hit the third button on the page to use the machine translation integration you set up earlier. Now since you set up the Wagtail Localize dummy translator, all it will do here is reverse all of the strings on the page. But it will give you an idea how Deepl or Google Cloud Translation would work if you set them up. If you use this option for your translation, you'll need to click back into the page and publish the results by clicking the "Publish in French" button.

## Translate and publish your pages

Using whichever method you prefer, go through and translate your "Blog" page as well as your "Badgers are brilliant" article. Be sure to publish each one of those pages after you finish adding your translations.

## Syncing content from your main language

Let's try syncing some changes from a blog written in your main language. In the lefthand menu, go to "Pages" then click the arrow to the right until you see "Badgers are brilliant". Play with the language switcher in the admin above it if you want to see how easy it is to switch between the languages. Click on the pencil to open the edit page for "Badgers are brilliant".

![Screenshot of an example of the admin language switcher](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-13_at_7.07.57_AM.original.png)


Scroll down to the body. You're going to add the link to this [YouTube video](https://www.youtube.com/watch?v=c36UNSoJenI) about an escape artist badger to the line "They can break out of zoos." Add the link by highlighting the text and selecting the link option from the menu. When the link menu pops up, click "External link" to add the link to text.

Publish the page with the new changes. After you hit Publish, you'll be returned to the menu for the "Blog" parent page. Hover over "Badgers are brilliant" and click the "More" button. Select "Sync translated pages."

![Screenshot of syncing translated pages](https://www.meagenvoss.com/media/images/Screen_Shot_2022-10-03_at_5.17.00_PM.original.png)

After you set up the sync, navigate to the French version of the page. Your changes to the content will be highlighted in yellow and you can translate them or insert local content. Notice how links and images are separated from the text and can be changed to make them more appealing to a French audience. For example, if you wanted to include a link to a video that was in French or that had French subtitles switched on, you could include a unique link in the French version of the blog. You're welcome to try this by including a link to a different video in the French version. Perhaps this video on [European badgers](https://www.youtube.com/watch?v=PvpNx0Hxtdk) would be more appropriate for your French audience.

All right. Now that we've added some content to your blog and translated it into French, we're going to add a translatable menu and a translatable footer to our website so that you can see how Snippets work in Wagtail as well as how you can translate them.
