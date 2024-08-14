import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    # Load the contents of the YAML file into a Python dictionary
    yaml_data = yaml.safe_load(file)

    # Create the root element of the XML document with the tag 'rss' and attributes
    rss_element = xml_tree.Element('rss', {
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
    })

    # Create a sub-element 'channel' under the 'rss' root element
    channel_element = xml_tree.SubElement(rss_element, 'channel')

    # Extract the link prefix from YAML data
    link_prefix = yaml_data.get('link', '')

    # Fill in the channel metadata using data from the YAML file
    xml_tree.SubElement(channel_element, 'title').text = yaml_data.get('title', '')
    xml_tree.SubElement(channel_element, 'format').text = yaml_data.get('format', '')
    xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data.get('subtitle', '')
    xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data.get('author', '')
    xml_tree.SubElement(channel_element, 'description').text = yaml_data.get('description', '')
    xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data.get('image', '')}) 
    xml_tree.SubElement(channel_element, 'language').text = yaml_data.get('language', '')
    xml_tree.SubElement(channel_element, 'link').text = link_prefix

    xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data.get('category', '')}) 

    # Loop over each item in the 'item' list from the YAML data
    for item in yaml_data.get('item', []):
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = item.get('title', '')
        xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data.get('author', '')
        xml_tree.SubElement(item_element, 'description').text = item.get('description', '')
        xml_tree.SubElement(item_element, 'itunes:duration').text = item.get('duration', '')
        xml_tree.SubElement(item_element, 'pubDate').text = item.get('published', '')
        
        # Create an 'enclosure' sub-element with attributes
        xml_tree.SubElement(item_element, 'enclosure', {
            'url': link_prefix + item.get('file', ''),
            'type': 'audio/mpeg',
            'length': item.get('length', '')
        })

    # Create an ElementTree object from the 'rss_element'
    output_tree = xml_tree.ElementTree(rss_element)

    # Write the XML data to a file named 'podcast.xml'
    output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
