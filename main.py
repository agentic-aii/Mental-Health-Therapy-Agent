{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "import getpass\n",
    "import os\n",
    "\n",
    "if \"GOOGLE_API_KEY\" not in os.environ:\n",
    "    os.environ[\"GOOGLE_API_KEY\"] = getpass.getpass(\"Enter your Google AI API key: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
