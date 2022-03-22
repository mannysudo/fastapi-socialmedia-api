"""create posts table

Revision ID: 49262cd9f6e7
Revises: 
Create Date: 2022-03-17 07:53:22.222028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49262cd9f6e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
